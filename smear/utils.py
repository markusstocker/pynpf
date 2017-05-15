from datetime import datetime, timedelta

# MATLAB datenum conversion
# Source: http://stackoverflow.com/questions/8776414/python-datetime-to-matlab-datenum
# Source: http://sociograph.blogspot.de/2011/04/how-to-avoid-gotcha-when-converting.html


def date2datenum(date):
    dt = datetime.strptime(date, '%Y-%m-%d')
    mdn = dt + timedelta(days=366)
    frac_seconds = (dt - datetime(dt.year, dt.month, dt.day, 0, 0, 0)).seconds / (24.0 * 60.0 * 60.0)
    frac_microseconds = dt.microsecond / (24.0 * 60.0 * 60.0 * 1000000.0)
    return mdn.toordinal() + frac_seconds + frac_microseconds


def datenum2date(dn):
    return datetime.fromordinal(int(dn)) + timedelta(days=dn % 1) - timedelta(days=366)
