email_pattern: str = r"""(
    [a-zA-Z-0-9._%+!~-]+ # username
    @
    [a-zA-Z-0-9.-]+ # domain name
    \.[a-zA-Z]{2,} # dot something
)"""
phone_no_pattern: str = r"\+\d{13}|d{11}"

american_no_pattern: str = r"""(
    (\(?\d{3}\)?) # area code, required
    (\s|-|\.)?    # separator
    (\d{3})       # first 3 digits
    (\s|-|\.)     # separator
    (\d{4})       # last 4 digits
    (\s*(ext|x|ext\.)\s*(\d{2,5}))? # optional extension
)"""