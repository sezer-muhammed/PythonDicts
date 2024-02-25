class RepresentableType(type):
    def __str__(cls):
        attrs = []
        for attr, value in cls.__dict__.items():
            if not attr.startswith('_'):
                attrs.append(f"{attr}={value}")
        return f"{cls.__name__}({', '.join(attrs)})"