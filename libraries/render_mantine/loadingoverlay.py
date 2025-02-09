from render import Component, create_callback, Props


class LoadingOverlay(Component):
    Module = "mantine"
    JSXName = "LoadingOverlay"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "exitTransitionDuration",
        "loader",
        "loaderProps",
        "m",
        "mb",
        "ml",
        "mr",
        "mt",
        "mx",
        "my",
        "overlayBlur",
        "overlayColor",
        "overlayOpacity",
        "p",
        "pb",
        "pl",
        "pr",
        "pt",
        "px",
        "py",
        "radius",
        "sx",
        "transitionDuration",
        "visible",
        "zIndex",
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
        exitTransitionDuration=None,
        loader=None,
        loaderProps=None,
        m=None,
        mb=None,
        ml=None,
        mr=None,
        mt=None,
        mx=None,
        my=None,
        overlayBlur=None,
        overlayColor=None,
        overlayOpacity=None,
        p=None,
        pb=None,
        pl=None,
        pr=None,
        pt=None,
        px=None,
        py=None,
        radius=None,
        sx=None,
        transitionDuration=None,
        visible=None,
        zIndex=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.exitTransitionDuration = exitTransitionDuration
        self.loader = loader
        self.loaderProps = loaderProps
        self.m = m
        self.mb = mb
        self.ml = ml
        self.mr = mr
        self.mt = mt
        self.mx = mx
        self.my = my
        self.overlayBlur = overlayBlur
        self.overlayColor = overlayColor
        self.overlayOpacity = overlayOpacity
        self.p = p
        self.pb = pb
        self.pl = pl
        self.pr = pr
        self.pt = pt
        self.px = px
        self.py = py
        self.radius = radius
        self.sx = sx
        self.transitionDuration = transitionDuration
        self.visible = visible
        self.zIndex = zIndex
