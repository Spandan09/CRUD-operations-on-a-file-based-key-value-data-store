# Base class for other custom exceptions
class exceptions(Exception):
    pass


class FileNotFound(exceptions):
    def __init__(self, message="File does not exist. Requires valid file path."):
        self.message = message
        super().__init__(self.message)


class FileNotAccessible(exceptions):
    def __init__(self, message="File can not be accessed. Requires file accessiblity to read or write."):
        self.message = message
        super().__init__(self.message)


class IOErrorOccurred(exceptions):
    def __init__(self, message="Caught IO Exception. File can not be accessed."):
        self.message = message
        super().__init__(self.message)


class InvalidKey(exceptions):
    def __init__(self, message="Key must be a string."):
        self.message = message
        super().__init__(self.message)


class KeyLengthExceeded(exceptions):
    def __init__(self, message="Requires valid Key not exceeding the maximum size of 32 characters."):
        self.message = message
        super().__init__(self.message)


class DuplicateKey(exceptions):
    def __init__(self, key, message=" already exists. Create is invoked for an existing key."):
        self.key = key
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.key} {self.message}'


class ValueSizeExceeded(exceptions):
    def __init__(self, message="Requires valid JSON object not exceeding the maximum size of 16KB."):
        self.message = message
        super().__init__(self.message)


class FileSizeExceeded(exceptions):
    def __init__(self, message="Reached Maximum file size. New data can not be stored."):
        self.message = message
        super().__init__(self.message)


class timeToLiveValueError(exceptions):
    def __init__(self, message="Invalid argument. Requires numerical value defining the number of seconds."):
        self.message = message
        super().__init__(self.message)


class EmptyFile(exceptions):
    def __init__(self, message="File does not have any json object."):
        self.message = message
        super().__init__(self.message)


class KeyNotExist(exceptions):
    def __init__(self, key, message="does not exist in database. Requires Valid Key."):
        self.message = message
        self.key = key
        super().__init__(self.message)

    def __str__(self):
        return f'Data associated with key value {self.key} {self.message}'


class KeyExpired(exceptions):
    def __init__(self, key, message="Key exceeded Time-To-Live. Can not be accessed for read, update or delete operation."):
        self.message = message
        super().__init__(self.message)


class KeyNotProvided(exceptions):
    def __init__(self, key, message="Key not provided. Key cannot be empty, entry a value."):
        self.message = message
        super().__init__(self.message)
