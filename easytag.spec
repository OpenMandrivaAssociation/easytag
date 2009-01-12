Summary:	Tag editor for MP3, OGG files
Name:		easytag
Version:	2.1.6
Release:	%mkrel 4
License:	GPLv2+
Group:		Sound
URL:		http://easytag.sourceforge.net
Source0:	http://prdownloads.sourceforge.net/easytag/%{name}-%{version}.tar.bz2
Source1:	easytag-2.1.6-de.po.bz2
Patch: 		easytag-2.1.6-mp4v2.patch
BuildRequires:	gtk2-devel >= 2.4
BuildRequires:	id3lib-devel
BuildRequires:	libid3tag-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libflac-devel
BuildRequires:	libwavpack-devel
BuildRequires:	libspeex-devel
BuildRequires:	libmp4v2-devel
Requires(post):	desktop-file-utils
Requires(postun):	desktop-file-utils
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
EasyTAG is an utility for viewing and editing tags of MP3, MP2, FLAC,
Ogg Vorbis, MP4/AAC, MusePack, Wavpack, Speex and Monkey's Audio
files. Its simple and nice GTK+ interface makes tagging easier under
GNU/Linux.
Features:
- View, edit, write tags of MP3, MP2 files (ID3 tag with pictures),
  FLAC files (FLAC Vorbis tag), Ogg Vorbis files (Ogg Vorbis tag),
  MP4/AAC (MP4/AAC tag), and MusePack, Wavpack, Monkey's Audio files
  (APE tag), Speex files,
- Can edit more tag fields : Title, Artist, Album, Disc Album, Year,
  Track Number, Genre, Comment, Composer, Original Artist/Performer,
  Copyright, URL and Encoder name,
- Auto tagging: parse filename and directory to complete automatically
  the fields (using masks),
- Ability to rename files and directories from the tag (using masks) or by
  loading a text file,
- Process selected files of the selected directory,
- Ability to browse subdirectories,
- Recursion for tagging, removing, renaming, saving...,
- Can set a field (artist, title,...) to all other files,
- Read file header informations (bitrate, time, ...) and display them,
- Auto completion of the date if a partial is entered,
- Undo and redo last changes,
- Ability to process fields of tag and file name (convert letters into
  uppercase, downcase, ...),
- Ability to open a directory or a file with an external program,
- CDDB support using Freedb.org servers (manual and automatic search),
- A tree based browser or a view by Artist & Album,
- A list to select files,
- A playlist generator window,
- A file searching window,
- Simple and explicit interface!,
- French, German, Russian, Dutch, Hungarian, Swedish, Italian, Japanese,
  Ukrainian, Czech, Spanish, Polish, Romanian, Danish, Greek and Brazilian
  Portuguese translation languages,
- Written in C and uses GTK+ 2.4 for the GUI.

%prep
%setup -q
bzcat %SOURCE1 > po/de.po
%patch -p1
autoreconf

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%update_desktop_database
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%clean_desktop_database
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc ChangeLog README TODO THANKS USERS-GUIDE
%doc doc/EasyTAG_Documentation* doc/users_guide*
%{_bindir}/easytag
%{_mandir}/man1/easytag.1*
%{_datadir}/applications/easytag.desktop
%{_datadir}/pixmaps/*
%{_datadir}/easytag/
