module.exports.readVersion = contents =>
    contents.match(/version = "(?<version>[^"]*)"/).groups.version

module.exports.writeVersion = (contents, version) =>
    contents.replace(/(.*version = ")[^"]*(".*)/, `$1${version}$2`)
