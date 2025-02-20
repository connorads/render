from render import Component, create_callback, InputComponent, Props


class Switch(InputComponent):
    Module = "mantine"
    JSXName = "Switch"
    InputName = "checked"
    CALLBACKS = ["onKeyPress", "onClick", "onLabel"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "color",
        "description",
        "error",
        "label",
        "labelPosition",
        "m",
        "mb",
        "ml",
        "mr",
        "mt",
        "mx",
        "my",
        "offLabel",
        "p",
        "pb",
        "pl",
        "pr",
        "pt",
        "px",
        "py",
        "radius",
        "size",
        "sx",
        "thumbIcon",
        "wrapperProps",
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
        onChange=None,
        defaultChecked=None,
        checked=None,
        color=None,
        description=None,
        error=None,
        label=None,
        labelPosition=None,
        m=None,
        mb=None,
        ml=None,
        mr=None,
        mt=None,
        mx=None,
        my=None,
        offLabel=None,
        onLabel=None,
        p=None,
        pb=None,
        pl=None,
        pr=None,
        pt=None,
        px=None,
        py=None,
        radius=None,
        size=None,
        sx=None,
        thumbIcon=None,
        wrapperProps=None,
        controller=None,
    ):
        super().__init__(key, controller, onChange, checked, defaultChecked)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.color = color
        self.description = description
        self.error = error
        self.label = label
        self.labelPosition = labelPosition
        self.m = m
        self.mb = mb
        self.ml = ml
        self.mr = mr
        self.mt = mt
        self.mx = mx
        self.my = my
        self.offLabel = offLabel
        self.onLabel = create_callback(onLabel, "onLabel")
        self.p = p
        self.pb = pb
        self.pl = pl
        self.pr = pr
        self.pt = pt
        self.px = px
        self.py = py
        self.radius = radius
        self.size = size
        self.sx = sx
        self.thumbIcon = thumbIcon
        self.wrapperProps = wrapperProps


class SwitchGroup(InputComponent):
    Module = "mantine"
    JSXName = "SwitchGroup"
    InputName = "value"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "m",
        "mb",
        "ml",
        "mr",
        "mt",
        "mx",
        "my",
        "offset",
        "orientation",
        "p",
        "pb",
        "pl",
        "pr",
        "pt",
        "px",
        "py",
        "size",
        "spacing",
        "sx",
        "wrapperProps",
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
        onChange=None,
        defaultValue=None,
        value=None,
        m=None,
        mb=None,
        ml=None,
        mr=None,
        mt=None,
        mx=None,
        my=None,
        offset=None,
        orientation=None,
        p=None,
        pb=None,
        pl=None,
        pr=None,
        pt=None,
        px=None,
        py=None,
        size=None,
        spacing=None,
        sx=None,
        wrapperProps=None,
        controller=None,
    ):
        super().__init__(key, controller, onChange, value, defaultValue)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.m = m
        self.mb = mb
        self.ml = ml
        self.mr = mr
        self.mt = mt
        self.mx = mx
        self.my = my
        self.offset = offset
        self.orientation = orientation
        self.p = p
        self.pb = pb
        self.pl = pl
        self.pr = pr
        self.pt = pt
        self.px = px
        self.py = py
        self.size = size
        self.spacing = spacing
        self.sx = sx
        self.wrapperProps = wrapperProps
