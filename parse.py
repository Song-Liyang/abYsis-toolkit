def get_headers(header_raw):
    """
    通过原生请求头获取请求头字典，即冒号形式
    :param header_raw: {str} 浏览器请求头
    :return: {dict} headers
    """
    return dict(line.split(": ", 1) for line in header_raw.split("\n"))


def get_cookies(cookie_raw):
    """
    通过原生cookie获取cookie字段,即等号形式
    :param cookie_raw: {str} 浏览器原始cookie
    :return: {dict} cookies
    """
    return dict(line.split("=", 1) for line in cookie_raw.split("; "))

input = 'uid=ID365334&selectedColour=Taylor&scheme_name=kabat&region_def_name=kabat&format=summary_format&aa_sequence=QEQLVQSGAEVKKPGSSVRVSCKASGGTFSGHHAIGWVRQAPGQGLEWMGGIIPIFGIANYAQKFQGRVMFTADKSTSTAYMELSSLRSADTAVYYCARDPDYYGSGTYQGWYFDLWGRGTLVAVSS&organism_id=not_selected'

output = get_cookies(input)

print(output)