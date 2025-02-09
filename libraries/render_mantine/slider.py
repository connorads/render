from render import Component, create_callback, InputComponent


class RangeSlider(InputComponent):
    Module = "mantine"
    JSXName = "RangeSlider"
    InputName = "value"
    CALLBACKS = ["onKeyPress", "onClick", "onChangeEnd"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "color",
        "disabled",
        "inverted",
        "label",
        "labelAlwaysOn",
        "labelTransition",
        "labelTransitionDuration",
        "labelTransitionTimingFunction",
        "m",
        "marks",
        "max",
        "mb",
        "min",
        "minRange",
        "ml",
        "mr",
        "mt",
        "mx",
        "my",
        "name",
        "p",
        "pb",
        "pl",
        "pr",
        "precision",
        "pt",
        "px",
        "py",
        "radius",
        "scale",
        "showLabelOnHover",
        "size",
        "step",
        "sx",
        "thumbChildren",
        "thumbFromLabel",
        "thumbSize",
        "thumbToLabel",
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
        color=None,
        disabled=None,
        inverted=None,
        label=None,
        labelAlwaysOn=None,
        labelTransition=None,
        labelTransitionDuration=None,
        labelTransitionTimingFunction=None,
        m=None,
        marks=None,
        max=None,
        mb=None,
        min=None,
        minRange=None,
        ml=None,
        mr=None,
        mt=None,
        mx=None,
        my=None,
        name=None,
        onChangeEnd=None,
        p=None,
        pb=None,
        pl=None,
        pr=None,
        precision=None,
        pt=None,
        px=None,
        py=None,
        radius=None,
        scale=None,
        showLabelOnHover=None,
        size=None,
        step=None,
        sx=None,
        thumbChildren=None,
        thumbFromLabel=None,
        thumbSize=None,
        thumbToLabel=None,
        controller=None,
    ):
        super().__init__(key, controller, onChange, value, defaultValue)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.color = color
        self.disabled = disabled
        self.inverted = inverted
        self.label = label
        self.labelAlwaysOn = labelAlwaysOn
        self.labelTransition = labelTransition
        self.labelTransitionDuration = labelTransitionDuration
        self.labelTransitionTimingFunction = labelTransitionTimingFunction
        self.m = m
        self.marks = marks
        self.max = max
        self.mb = mb
        self.min = min
        self.minRange = minRange
        self.ml = ml
        self.mr = mr
        self.mt = mt
        self.mx = mx
        self.my = my
        self.name = name
        self.onChangeEnd = create_callback(onChangeEnd, "onChangeEnd")
        self.p = p
        self.pb = pb
        self.pl = pl
        self.pr = pr
        self.precision = precision
        self.pt = pt
        self.px = px
        self.py = py
        self.radius = radius
        self.scale = scale
        self.showLabelOnHover = showLabelOnHover
        self.size = size
        self.step = step
        self.sx = sx
        self.thumbChildren = thumbChildren
        self.thumbFromLabel = thumbFromLabel
        self.thumbSize = thumbSize
        self.thumbToLabel = thumbToLabel


class Slider(InputComponent):
    Module = "mantine"
    JSXName = "Slider"
    InputName = "value"
    CALLBACKS = ["onKeyPress", "onClick", "onChangeEnd"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "color",
        "disabled",
        "inverted",
        "label",
        "labelAlwaysOn",
        "labelTransition",
        "labelTransitionDuration",
        "labelTransitionTimingFunction",
        "m",
        "marks",
        "max",
        "mb",
        "min",
        "ml",
        "mr",
        "mt",
        "mx",
        "my",
        "name",
        "p",
        "pb",
        "pl",
        "pr",
        "precision",
        "pt",
        "px",
        "py",
        "radius",
        "scale",
        "showLabelOnHover",
        "size",
        "step",
        "sx",
        "thumbChildren",
        "thumbLabel",
        "thumbSize",
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
        color=None,
        disabled=None,
        inverted=None,
        label=None,
        labelAlwaysOn=None,
        labelTransition=None,
        labelTransitionDuration=None,
        labelTransitionTimingFunction=None,
        m=None,
        marks=None,
        max=None,
        mb=None,
        min=None,
        ml=None,
        mr=None,
        mt=None,
        mx=None,
        my=None,
        name=None,
        onChangeEnd=None,
        p=None,
        pb=None,
        pl=None,
        pr=None,
        precision=None,
        pt=None,
        px=None,
        py=None,
        radius=None,
        scale=None,
        showLabelOnHover=None,
        size=None,
        step=None,
        sx=None,
        thumbChildren=None,
        thumbLabel=None,
        thumbSize=None,
        controller=None,
    ):
        super().__init__(key, controller, onChange, value, defaultValue)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.color = color
        self.disabled = disabled
        self.inverted = inverted
        self.label = label
        self.labelAlwaysOn = labelAlwaysOn
        self.labelTransition = labelTransition
        self.labelTransitionDuration = labelTransitionDuration
        self.labelTransitionTimingFunction = labelTransitionTimingFunction
        self.m = m
        self.marks = marks
        self.max = max
        self.mb = mb
        self.min = min
        self.ml = ml
        self.mr = mr
        self.mt = mt
        self.mx = mx
        self.my = my
        self.name = name
        self.onChangeEnd = create_callback(onChangeEnd, "onChangeEnd")
        self.p = p
        self.pb = pb
        self.pl = pl
        self.pr = pr
        self.precision = precision
        self.pt = pt
        self.px = px
        self.py = py
        self.radius = radius
        self.scale = scale
        self.showLabelOnHover = showLabelOnHover
        self.size = size
        self.step = step
        self.sx = sx
        self.thumbChildren = thumbChildren
        self.thumbLabel = thumbLabel
        self.thumbSize = thumbSize
