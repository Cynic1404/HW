class Tag:
    def __init__(self, tag, klass=None, **kwargs):
        self.tag = tag
        self.text = ""
        self.attributes = {}

        if klass is not None:
            self.attributes["class"] = " ".join(klass)

        for attr, value in kwargs.items():
            if "_" in attr:
                attr = attr.replace("_", "-")
            self.attributes[attr] = value

    def __str__(self):
        attrs = []
        for attribute, value in self.attributes.items():
            attrs.append('%s="%s"' % (attribute,value))
        attrs = " ".join(attrs)
        return "<{tag} {attrs}>\n{text}\n</{tag}>".format(
            tag=self.tag, attrs=attrs, text=self.text
        )

paragraph = Tag(
    "p",
    klass=("text-align-right", "text-nice"),
    id="heading-text",
    data_bind="not-above"
)
paragraph.text = "Some text inside tag"
print(paragraph)