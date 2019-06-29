# coding:utf-8

class RET:
    OK = "200"
    CREATED = "201"
    ACCEPTED = "202"
    NOCONTENT = "204"

    MOVEDPERMANENTLY = "301"
    SEEOTHER = "303"
    NOTMODIFIED = "304"

    BADREQUEST = "400"
    UNAUTHORIZED = "401"
    FORBIDDEN = "403"
    NOTFOUND = "404"
    METHODNOTALLOWED = "405"
    NOTACCEPTABLE = "406"
    CONFLICT = "409"

    INTERNALSERVERERROR = "500"
    SERVICEUNAVAILABLE = "503"

    DBERR = "4001"
    NODATA = "4002"
    DATAEXIST = "4003"
    DATAERR = "4004"

    SESSIONERR = "4101"
    LOGINERR = "4102"
    PARAMERR = "4103"
    USERERR = "4104"
    ROLEERR = "4105"
    PWDERR = "4106"

    REQERR = "4201"
    IPERR = "4202"

    THIRDERR = "4301"
    IOERR = "4302"

    SERVERERR = "4500"
    UNKOWNERR = "4501"


error_map = {

    RET.OK: u"请求成功",
    RET.CREATED: u'创建成功',
    RET.ACCEPTED: u'更新成功',
    RET.NOCONTENT: u'表示资源有空',

    RET.MOVEDPERMANENTLY: u'资源的URI已被更新',
    RET.SEEOTHER: u'其他（如，负载均衡)',
    RET.NOTMODIFIED: u'资源未更改（缓存）',

    RET.BADREQUEST: u'坏请求（如，参数错误）',
    RET.UNAUTHORIZED: u'未授权',
    RET.FORBIDDEN: u'被禁止访问',
    RET.NOTFOUND: u'请求的资源不存在',
    RET.METHODNOTALLOWED: u'请求方法对指定的资源不适用',
    RET.NOTACCEPTABLE: u'请求格式错误',
    RET.CONFLICT: u'通用冲突',

    RET.INTERNALSERVERERROR: u'内部错误',
    RET.SERVICEUNAVAILABLE: u'服务当前无法处理请求',

    RET.DBERR: u"数据库查询错误",
    RET.NODATA: u"无数据",
    RET.DATAEXIST: u"数据已存在",
    RET.DATAERR: u"数据错误",

    RET.SESSIONERR: u"用户未登录",
    RET.LOGINERR: u"用户登录失败",
    RET.PARAMERR: u"参数错误",
    RET.USERERR: u"用户不存在或未激活",
    RET.ROLEERR: u"用户身份错误",
    RET.PWDERR: u"密码错误",

    RET.REQERR: u"非法请求或请求次数受限",
    RET.IPERR: u"IP受限",

    RET.THIRDERR: u"第三方系统错误",
    RET.IOERR: u"文件读写错误",

    RET.SERVERERR: u"内部错误",
    RET.UNKOWNERR: u"未知错误",
}

# 所有 HTTP 状态码
error_message = {
    100: 'Continue',
    101: 'Switching Protocols',
    102: 'Processing',
    200: 'OK',
    201: 'Created',
    202: 'Accepted',
    203: 'Non Authoritative Information',
    204: 'No Content',
    205: 'Reset Content',
    206: 'Partial Content',
    207: 'Multi Status',
    226: 'IM Used',
    300: 'Multiple Choices',
    301: 'Moved Permanently',
    302: 'Found',
    303: 'See Other',
    304: 'Not Modified',
    305: 'Use Proxy',
    307: 'Temporary Redirect',
    308: 'Permanent Redirect',
    400: 'Bad Request',
    401: 'Unauthorized',
    402: 'Payment Required',
    403: 'Forbidden',
    404: 'Not Found',
    405: 'Method Not Allowed',
    406: 'Not Acceptable',
    407: 'Proxy Authentication Required',
    408: 'Request Timeout',
    409: 'Conflict',
    410: 'Gone',
    411: 'Length Required',
    412: 'Precondition Failed',
    413: 'Request Entity Too Large',
    414: 'Request URI Too Long',
    415: 'Unsupported Media Type',
    416: 'Requested Range Not Satisfiable',
    417: 'Expectation Failed',
    418: "I'm a teapot",
    421: 'Misdirected Request',
    422: 'Unprocessable Entity',
    423: 'Locked',
    424: 'Failed Dependency',
    426: 'Upgrade Required',
    428: 'Precondition Required',
    429: 'Too Many Requests',
    431: 'Request Header Fields Too Large',
    449: 'Retry With',
    451: 'Unavailable For Legal Reasons',
    500: 'Internal Server Error',
    501: 'Not Implemented',
    502: 'Bad Gateway',
    503: 'Service Unavailable',
    504: 'Gateway Timeout',
    505: 'HTTP Version Not Supported',
    507: 'Insufficient Storage',
    510: 'Not Extended'
}
