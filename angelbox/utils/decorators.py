def require_root(func):
    """Decorator to require root privileges"""
    def wrapper(shell, *args, **kwargs):
        if not shell.user.get('is_root', False):
            print(f"Error: {func.__name__} requires root privileges!")
            return
        return func(shell, *args, **kwargs)
    return wrapper