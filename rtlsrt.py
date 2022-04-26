import srt
import unicodedata


class RtlSrt:
    def __init__(self, file=None, srt_content=None):
        self.file = file
        self.srt_content = srt_content
        if (srt_content is None and file is not None):
            self.parse()

    def parse(self):
        self.srt_content = list(srt.parse(self.file))

    def fix_rtl(self):
        rtl_embedding = "\N{Right-To-Left Embedding}"
        for block in self.srt_content:
            content = list()
            for line in block.content.splitlines():
                line = line.replace(rtl_embedding, '')
                if self._contain_persian_letter(line):
                    content.append(rtl_embedding + line)
                else:
                    content.append(line)
            block.content = "\n".join(content)

    @staticmethod
    def _contain_persian_letter(text):
        unicodedataset = set(map(unicodedata.name, text))
        matches = ['arabic', 'persian']
        if any(map(lambda x: any(match in x.lower() for match in matches), unicodedataset)):
            return True
        return False

    def compose(self):
        return srt.compose(self.srt_content)
