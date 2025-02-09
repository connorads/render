from render import Component, create_callback


class Burger(Component):
    Module = "mantine"
    JSXName = "Burger"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "color",
        "m",
        "mb",
        "ml",
        "mr",
        "mt",
        "mx",
        "my",
        "opened",
        "p",
        "pb",
        "pl",
        "pr",
        "pt",
        "px",
        "py",
        "size",
        "sx",
        "transitionDuration",
    ]

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        color=None,
        m=None,
        mb=None,
        ml=None,
        mr=None,
        mt=None,
        mx=None,
        my=None,
        opened=None,
        p=None,
        pb=None,
        pl=None,
        pr=None,
        pt=None,
        px=None,
        py=None,
        size=None,
        sx=None,
        transitionDuration=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.color = color
        self.m = m
        self.mb = mb
        self.ml = ml
        self.mr = mr
        self.mt = mt
        self.mx = mx
        self.my = my
        self.opened = opened
        self.p = p
        self.pb = pb
        self.pl = pl
        self.pr = pr
        self.pt = pt
        self.px = px
        self.py = py
        self.size = size
        self.sx = sx
        self.transitionDuration = transitionDuration
