
class Snapshot(dict):
      def __init__(self, urlkey=None, timestamp=None, original=None, mimetype=None, statuscode=None, digest=None, length=None):
            super(Snapshot, self).__init__()
            self['urlkey'] = urlkey
            self['timestamp'] = timestamp
            self['original'] = original
            self['mimetype'] = mimetype
            self['statuscode'] = statuscode
            self['digest'] = digest
            self['length'] = length
            self['snapshot_url'] = 'http://web.archive.org/web/%s/%s/' % (timestamp, original)
            self['usefulness'] = 1
            self['same_as'] = None