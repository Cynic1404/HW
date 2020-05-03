class Tag:
    def __init__(self, tag, is_single=False):
        self.tag = tag
        self.text = ""
        self.attributes = {}
        self.is_single = is_single

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        attrs = []
        for attribute, value in self.attributes.items():
            attrs.append('%s="%s"' % (attribute, value))
        attrs = " ".join(attrs)

        if self.is_single:
            print("<{tag} {attrs}/>".format(tag=self.tag, attrs=attrs))
        else:
            print(
                "<{tag} {attrs}>{text}</{tag}>".format(
                    tag=self.tag, attrs=attrs, text=self.text
                )
            )


with Tag("H1") as tag:
    tag.text = "Привет"
    tag.attributes["class"] = "my_amazing_class"