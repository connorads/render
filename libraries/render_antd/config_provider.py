from render import Component, create_callback


class Usage(Component):
    Module = "ant"
    JSXName = "Usage"
    CALLBACKS = ["onKeyPress", "onClick", "wave"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "alert",
        "anchor",
        "autoInsertSpaceInButton",
        "avatar",
        "badge",
        "breadcrumb",
        "button",
        "calendar",
        "card",
        "carousel",
        "cascader",
        "checkbox",
        "collapse",
        "colorPicker",
        "componentDisabled",
        "componentSize",
        "csp",
        "datePicker",
        "descriptions",
        "direction",
        "divider",
        "drawer",
        "empty",
        "flex",
        "form",
        "getPopupContainer",
        "getTargetContainer",
        "iconPrefixCls",
        "image",
        "input",
        "layout",
        "list",
        "locale",
        "mentions",
        "menu",
        "message",
        "modal",
        "notification",
        "pagination",
        "popupMatchSelectWidth",
        "popupOverflow",
        "prefixCls",
        "progress",
        "radio",
        "rate",
        "renderEmpty",
        "result",
        "segmented",
        "select",
        "skeleton",
        "slider",
        "space",
        "spin",
        "statistic",
        "steps",
        "switch",
        "table",
        "tabs",
        "tag",
        "theme",
        "timePicker",
        "timeline",
        "transfer",
        "tree",
        "typography",
        "upload",
        "virtual",
        "warning",
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
        alert=None,
        anchor=None,
        autoInsertSpaceInButton=None,
        avatar=None,
        badge=None,
        breadcrumb=None,
        button=None,
        calendar=None,
        card=None,
        carousel=None,
        cascader=None,
        checkbox=None,
        collapse=None,
        colorPicker=None,
        componentDisabled=None,
        componentSize=None,
        csp=None,
        datePicker=None,
        descriptions=None,
        direction=None,
        divider=None,
        drawer=None,
        empty=None,
        flex=None,
        form=None,
        getPopupContainer=None,
        getTargetContainer=None,
        iconPrefixCls=None,
        image=None,
        input=None,
        layout=None,
        list=None,
        locale=None,
        mentions=None,
        menu=None,
        message=None,
        modal=None,
        notification=None,
        pagination=None,
        popupMatchSelectWidth=None,
        popupOverflow=None,
        prefixCls=None,
        progress=None,
        radio=None,
        rate=None,
        renderEmpty=None,
        result=None,
        segmented=None,
        select=None,
        skeleton=None,
        slider=None,
        space=None,
        spin=None,
        statistic=None,
        steps=None,
        switch=None,
        table=None,
        tabs=None,
        tag=None,
        theme=None,
        timePicker=None,
        timeline=None,
        transfer=None,
        tree=None,
        typography=None,
        upload=None,
        virtual=None,
        warning=None,
        wave=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.alert = alert
        self.anchor = anchor
        self.autoInsertSpaceInButton = autoInsertSpaceInButton
        self.avatar = avatar
        self.badge = badge
        self.breadcrumb = breadcrumb
        self.button = button
        self.calendar = calendar
        self.card = card
        self.carousel = carousel
        self.cascader = cascader
        self.checkbox = checkbox
        self.collapse = collapse
        self.colorPicker = colorPicker
        self.componentDisabled = componentDisabled
        self.componentSize = componentSize
        self.csp = csp
        self.datePicker = datePicker
        self.descriptions = descriptions
        self.direction = direction
        self.divider = divider
        self.drawer = drawer
        self.empty = empty
        self.flex = flex
        self.form = form
        self.getPopupContainer = getPopupContainer
        self.getTargetContainer = getTargetContainer
        self.iconPrefixCls = iconPrefixCls
        self.image = image
        self.input = input
        self.layout = layout
        self.list = list
        self.locale = locale
        self.mentions = mentions
        self.menu = menu
        self.message = message
        self.modal = modal
        self.notification = notification
        self.pagination = pagination
        self.popupMatchSelectWidth = popupMatchSelectWidth
        self.popupOverflow = popupOverflow
        self.prefixCls = prefixCls
        self.progress = progress
        self.radio = radio
        self.rate = rate
        self.renderEmpty = renderEmpty
        self.result = result
        self.segmented = segmented
        self.select = select
        self.skeleton = skeleton
        self.slider = slider
        self.space = space
        self.spin = spin
        self.statistic = statistic
        self.steps = steps
        self.switch = switch
        self.table = table
        self.tabs = tabs
        self.tag = tag
        self.theme = theme
        self.timePicker = timePicker
        self.timeline = timeline
        self.transfer = transfer
        self.tree = tree
        self.typography = typography
        self.upload = upload
        self.virtual = virtual
        self.warning = warning
        self.wave = create_callback(wave, "wave")
