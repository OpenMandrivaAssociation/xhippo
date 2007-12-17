%define name xhippo
%define version 3.3
%define release %mkrel 4

Name: %{name}
Summary: A mp3 playlist frontend
Version: %{version}
Release: %{release}
Source: ftp://ftp.free.fr/gnu/xhippo/%{name}-%{version}.tar.bz2
Source1: %{name}-16x16.png.bz2
Source2: %{name}-32x32.png.bz2
Source3: %{name}-48x48.png.bz2
Group: Sound 
License: GPL
BuildRequires: libgtk+-devel 
Url: http://www.gnu.org/software/xhippo/xhippo.html

%description
Xhippo is a Mp3 playlist frontend.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q

%build

%configure 

%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
cp xhippo.config $RPM_BUILD_ROOT%{_sysconfdir}
%find_lang %{name}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{title}
Comment=%{summary}
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=GTK;Audio;X-MandrivaLinux-Multimedia-Audio;
EOF

#icons
mkdir -p $RPM_BUILD_ROOT{%{_iconsdir},%{_miconsdir},%{_liconsdir}}
bzcat %{SOURCE1} > $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
bzcat %{SOURCE2} > $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
bzcat %{SOURCE3} > $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%post
%{update_menus}
 
%postun
%{clean_menus} 

%files -f %name.lang
%defattr(-,root,root)
%doc doc/*.* README ChangeLog AUTHORS BUGS COPYING NEWS README* TODO
%config(noreplace) %{_sysconfdir}/xhippo.config
%{_bindir}/xhippo
%{_datadir}/applications/mandriva-%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%_mandir/man1/*

%clean
rm -rf $RPM_BUILD_ROOT 


