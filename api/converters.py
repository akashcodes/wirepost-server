
class FourDigitYearConverter:
    regex = '[0-9]{4}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%04d' % value


class TwoDigitMonthConverter:
    regex = '1[0-2]|0[1-9]|[1-9]'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%02d' % value


class TwoDigitDateConverter:
    regex = '1[0-9]|2[0-9]|3[0-1]|0[1-9]|[1-9]'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%02d' % value