# What's dis

A little thing I had to do for *ahem* reasons for an undisclosed entity.

It's just a set implementation with versioning.  The underlying storage is
a dict (this entity reasonably didn't let me use a set, though using a dict
isn't much harder).

To fetch a version, we traverse the history either forwards or backwards
depending on how far back in history we need to go.

I also added typing for fun.

Is this useful? No, but I had an itch.
