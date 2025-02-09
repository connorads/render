from render import Component, create_callback


class Upload(Component):
    Module = "ant"
    JSXName = "Upload"
    CALLBACKS = [
        "onKeyPress",
        "onClick",
        "action",
        "beforeUpload",
        "onChange",
        "onDownload",
        "onDrop",
        "onPreview",
        "onRemove",
        "previewFile",
    ]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "accept",
        "customRequest",
        "data",
        "defaultFileList",
        "directory",
        "disabled",
        "fileList",
        "headers",
        "iconRender",
        "isImageUrl",
        "itemRender",
        "listType",
        "maxCount",
        "method",
        "multiple",
        "name",
        "openFileDialogOnClick",
        "progress",
        "showUploadList",
        "withCredentials",
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
        accept=None,
        action=None,
        beforeUpload=None,
        customRequest=None,
        data=None,
        defaultFileList=None,
        directory=None,
        disabled=None,
        fileList=None,
        headers=None,
        iconRender=None,
        isImageUrl=None,
        itemRender=None,
        listType=None,
        maxCount=None,
        method=None,
        multiple=None,
        name=None,
        onChange=None,
        onDownload=None,
        onDrop=None,
        onPreview=None,
        onRemove=None,
        openFileDialogOnClick=None,
        previewFile=None,
        progress=None,
        showUploadList=None,
        withCredentials=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.accept = accept
        self.action = create_callback(action, "action")
        self.beforeUpload = create_callback(beforeUpload, "beforeUpload", [[0], [1]])
        self.customRequest = customRequest
        self.data = data
        self.defaultFileList = defaultFileList
        self.directory = directory
        self.disabled = disabled
        self.fileList = fileList
        self.headers = headers
        self.iconRender = iconRender
        self.isImageUrl = isImageUrl
        self.itemRender = itemRender
        self.listType = listType
        self.maxCount = maxCount
        self.method = method
        self.multiple = multiple
        self.name = name
        self.onChange = create_callback(onChange, "onChange")
        self.onDownload = create_callback(onDownload, "onDownload", [[0]])
        self.onDrop = create_callback(onDrop, "onDrop")
        self.onPreview = create_callback(onPreview, "onPreview", [[0]])
        self.onRemove = create_callback(onRemove, "onRemove", [[0]])
        self.openFileDialogOnClick = openFileDialogOnClick
        self.previewFile = create_callback(previewFile, "previewFile")
        self.progress = progress
        self.showUploadList = showUploadList
        self.withCredentials = withCredentials


class UploadFile(Component):
    Module = "ant"
    JSXName = "UploadFile"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "crossOrigin",
        "name",
        "percent",
        "status",
        "thumbUrl",
        "uid",
        "url",
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
        crossOrigin=None,
        name=None,
        percent=None,
        status=None,
        thumbUrl=None,
        uid=None,
        url=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.crossOrigin = crossOrigin
        self.name = name
        self.percent = percent
        self.status = status
        self.thumbUrl = thumbUrl
        self.uid = uid
        self.url = url
