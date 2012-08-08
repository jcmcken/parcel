======
Parcel
======

Package up what's here and shove it over there.

**Parcel** is a command-line utility for packing up a bunch of files as they
exist on one server and unpacking the files exactly onto another server.

Tutorial
--------

**Parcel** can work in two general ways, by dynamically creating and packing 
your files, or by packing according to a predefined file manifest.

To begin a dynamic manifest, just type::

    par --start

This will generate a dynamic manifest located at ``~/.parcel/.dyn``. You should
probably not manually alter this file. But if you need to manually remove it
for some reason, that's where it is.

The purpose of dynamic manifests is to allow you to jump around your system, 
adding files as you go::
   
    $ cd /etc
    $ par --add hosts group
    parcel: OK
    $ par --add /var/log/messages
    parcel: OK

If you made a mistake, you can always list your manifest, find the offending file,
and remove it::

    $ par --list
    /etc/hosts
    /etc/group
    /var/log/messages
    $ par --del /var/log/messages
    parcel: OK

When you're done, you can either save the manifest or begin packing. To save::

    $ par --save mymanifest
    parcel: saved dynamic manifest to 'mymanifest'!

To begin packing::

    $ par --pack mystuff.par
    parcel: successfully packed parcel 'mystuff.par'!

You can keep modifying your dynamic manifest if you want to, otherwise it's probably
safe to just clear it::

    $ par --clear
    parcel: OK
    $ par --list
    $ 

If you need to update a saved manifest, simply load it::

    $ par --list
    $ par --load mymanifest
    parcel: OK
    $ par --list
    /etc/hosts
    /etc/group

If you already have a manifest in mind (created via ``par --save``) that you'd like
to pack, you can simply do the following::

    $ par --pack mystuff.par --from mymanifest
    parcel: successfully packed parcel 'mystuff.par'

Once you've created a parcel, it would be useful to validate that it truly matches
the files on your system::

    $ par --validate mystuff.par
    parcel: OK

If there are any mode, file type, owner, group, size, or timestamp differences 
between the files in the parcel and the files on the system, those will be printed
on screen. Otherwise a standard ``parcel: OK`` message will be printed. This validation
is useful for deployments.

Finally, you probably need to know how to unpack a parcel::

    $ par --unpack mystuff.par
    parcel: OK

This will distribute the files exactly as they were found on the originating system. 
If you'd like to alter this behavior, you can pass the ``-C`` option to specify an
alternate prefix (besides ``\/``), and the files will be 'extracted' with respect
to that directory. 

With all parcel options, you can pass the ``-l/--log-level`` option to specify a log
level (the default is ``INFO``). This can aid in debugging any issues.

What Gets Stored
----------------

File Information
****************

When creating a parcel, the following file information is stored:

* File type (regular file, symlink, directory)
* Mode (e.g. ``0755``)
* File owner
* Group owner
* SELinux context label
* File size
* Modified Time

**Note**: If you're packing up symlinks, you must make sure to pack both the link and the
target, or the symlink will be pointing at nothing inside the parcel.

Metadata
********

Some global properties are also stored inside the parcel:

* Username of the issuer (person who created the parcel)
* Effective username of the issuer
* Date/time parcel finished packing
* FQDN of the host where the parcel originated
* A randomly generated ID to uniquely distinguish the parcel from others

To print this global metadata, pass ``--meta`` along with ``--list``, e.g.::

    $ par --list mystuff.par --meta
    effective_user: jcmcken
    datetime: 2007-03-01T13:00:00Z
    fqdn: localhost.localdomain
    id: 8cb6f4c48ed673f84492faa666f8743057df8eb3
    user: jcmcken

Additional arbitrary key/value pairs can be added to this built-in metadata 
during parcel creation time::

    $ par --pack mystuff.par -e status=testing 
    parcel: successfully packed parcel 'mystuff.par'!
    $ par --list mystuff.par --meta
    effective_user: jcmcken
    datetime: 2007-03-01T13:00:00Z
    fqdn: localhost.localdomain
    id: 8cb6f4c48ed673f84492faa666f8743057df8eb3
    status: production
    user: jcmcken

Manifest
********

The parcel's manifest also gets stored along with the files and other metadata. To
print a parcel's manifest, simply do the following::

    $ par --manifest mystuff.par
    /etc/hosts
    /etc/group
