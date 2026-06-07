class Singleton:
    """
    __new__ runs BEFORE __init__ — it creates the actual object.
    We override it here to ensure only one instance ever exists.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print(f"Creating first and only instance of {cls.__name__}")
            cls._instance = super().__new__(cls)
        else:
            print("Returning existing instance")
        return cls._instance

    def __init__(self, config: str):
        # This runs every time Singleton() is called — even for existing instances
        # Guard against re-initialisation
        if not hasattr(self, "_initialised"):
            self.config = config
            self._initialised = True

    # Called when the object is garbage collected — cleanup hook
    def __del__(self):
        print(f"Singleton instance being destroyed")


s1 = Singleton("production")
s2 = Singleton("staging")     # returns the same instance as s1

print(s1 is s2)        # True — same object in memory
print(s1.config)       # "production" — not overwritten
print(s2.config)       # "production" — same object