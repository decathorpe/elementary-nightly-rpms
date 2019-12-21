%global srcname terminal
%global appname io.elementary.terminal

Name:           elementary-terminal
Summary:        The terminal of the 21st century
Version:        5.4.0+git%{date}.%{commit}
Release:        1%{?dist}
License:        LGPLv3

URL:            https://github.com/elementary/%{srcname}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  appstream
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.40.0

BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.39
BuildRequires:  pkgconfig(granite) >= 5.2.0
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.9.10
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(vte-2.91)

Obsoletes:      pantheon-terminal
Provides:       pantheon-terminal


%description
A super lightweight, beautiful, and simple terminal. It's designed to be
setup with sane defaults and little to no configuration. It's just a
terminal, nothing more, nothing less.


%package        fish
Summary:        The terminal of the 21st century (fish support)

Requires:       %{name} = %{version}-%{release}
Requires:       fish

Supplements:    (%{name} and fish)

BuildArch:      noarch

%description    fish
A super lightweight, beautiful, and simple terminal. It's designed to be
setup with sane defaults and little to no configuration. It's just a
terminal, nothing more, nothing less.

This package contains the files needed to support "process completed"
notifications when using the fish shell.


%prep
%autosetup -p1


%build
%meson -Dubuntu-bionic-patched-vte=false
%meson_build


%install
%meson_install

%find_lang %{appname}


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/open-pantheon-terminal-here.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/appdata/%{appname}.appdata.xml || :


%files -f %{appname}.lang
%doc README.md
%license COPYING

%{_bindir}/%{appname}

%{_datadir}/applications/open-pantheon-terminal-here.desktop
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/%{appname}/
%{_datadir}/metainfo/%{appname}.appdata.xml

%files fish
%{_datadir}/fish/vendor_conf.d/pantheon_terminal_process_completion_notifications.fish


%changelog
* Sat Dec 21 2019 Fabio Valentini <decathorpe@gmail.com> - 5.4.0+git191221.175256.ed9b72f8-1
- Update to latest snapshot.

* Sat Dec 21 2019 Fabio Valentini <decathorpe@gmail.com> - 5.4.0+git191221.082235.004dba3c-1
- Update to latest snapshot.

* Thu Dec 19 2019 Fabio Valentini <decathorpe@gmail.com> - 5.4.0+git191219.195759.4054584d-1
- Update to latest snapshot.

* Wed Dec 18 2019 Fabio Valentini <decathorpe@gmail.com> - 5.4.0+git191218.195838.adac372c-1
- Update to latest snapshot.

* Wed Dec 18 2019 Fabio Valentini <decathorpe@gmail.com> - 5.4.0+git191218.100856.9ea1b9f3-1
- Update to latest snapshot.

* Tue Dec 17 2019 Fabio Valentini <decathorpe@gmail.com> - 5.4.0+git191217.002432.2e4ca5cb-1
- Update to latest snapshot.

* Mon Dec 16 2019 Fabio Valentini <decathorpe@gmail.com> - 5.4.0+git191216.190352.b3158348-1
- Update to latest snapshot.

* Mon Dec 16 2019 Fabio Valentini <decathorpe@gmail.com> - 5.4.0+git191216.182017.540f43bf-1
- Update to latest snapshot.

* Sat Dec 14 2019 Fabio Valentini <decathorpe@gmail.com> - 5.4.0+git191214.174103.f7b17e5a-1
- Update to latest snapshot.

* Tue Dec 10 2019 Fabio Valentini <decathorpe@gmail.com> - 5.4.0+git191210.205923.a811c271-1
- Update to latest snapshot.

* Wed Dec 04 2019 Fabio Valentini <decathorpe@gmail.com> - 5.4.0+git191204.212539.baddb724-1
- Update to latest snapshot.

* Wed Dec 04 2019 Fabio Valentini <decathorpe@gmail.com> - 5.4.0+git191204.045738.22665036-1
- Update to latest snapshot.

* Mon Dec 02 2019 Fabio Valentini <decathorpe@gmail.com> - 5.4.0+git191202.100707.0e5cfdf8-1
- Update to latest snapshot.

* Sun Dec 01 2019 Fabio Valentini <decathorpe@gmail.com> - 5.4.0+git191201.162023.6953441f-1
- Update to latest snapshot.

* Sun Dec 01 2019 Fabio Valentini <decathorpe@gmail.com> - 5.4.0+git191201.112459.c33263e6-1
- Update to latest snapshot.

* Fri Nov 22 2019 Fabio Valentini <decathorpe@gmail.com> - 5.4.0+git191122.032459.bbbdc0b1-1
- Update to latest snapshot.

* Tue Nov 19 2019 Fabio Valentini <decathorpe@gmail.com> - 5.4.0+git191119.212448.2c85d48e-1
- Update to latest snapshot.

* Mon Nov 18 2019 Fabio Valentini <decathorpe@gmail.com> - 5.4.0+git191118.212357.25988799-1
- Update to latest snapshot.

* Sun Nov 17 2019 Fabio Valentini <decathorpe@gmail.com> - 5.4.0+git191117.085051.09d9e83d-1
- Update to latest snapshot.

* Sat Nov 16 2019 Fabio Valentini <decathorpe@gmail.com> - 5.4.0+git191115.231123.4144a007-1
- Update to version 5.4.0.

* Sat Nov 16 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.6+git191115.231123.4144a007-1
- Update to latest snapshot.

* Thu Nov 14 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.6+git191114.112634.695faec7-1
- Update to latest snapshot.

* Mon Nov 11 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.6+git191111.122429.8f88e8c3-1
- Update to latest snapshot.

* Sat Nov 09 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.6+git191109.152431.dd2dae40-1
- Update to latest snapshot.

* Wed Nov 06 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.6+git191106.182643.e88a709c-1
- Update to latest snapshot.

* Wed Nov 06 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.6+git191106.173912.68cb5147-1
- Update to latest snapshot.

* Wed Nov 06 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.6+git191106.161814.5eb12e12-1
- Update to latest snapshot.

* Wed Oct 16 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.6+git191015.232723.f3132135-1
- Update to latest snapshot.

* Thu Oct 10 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.6+git191010.142341.56ce22da-1
- Update to latest snapshot.

* Tue Oct 08 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.6+git191008.224849.0185bf0a-1
- Update to latest snapshot.

* Tue Oct 08 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.6+git191008.215851.44de1a64-1
- Update to latest snapshot.

* Sat Oct 05 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.6+git191005.102324.43384cda-1
- Update to latest snapshot.

* Sat Oct 05 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.6+git191005.040849.e6ef6b54-1
- Update to latest snapshot.

* Thu Oct 03 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.6+git191003.173916.5c39b9b8-1
- Update to latest snapshot.

* Wed Oct 02 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.6+git191001.203118.62058350-2
- Remove dropped AUTHORS file.

* Tue Oct 01 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.6+git191001.203118.62058350-1
- Update to latest snapshot.

* Tue Sep 24 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.6+git190924.181929.4f520ce7-1
- Update to latest snapshot.

* Thu Sep 19 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.6+git190919.180112.76c1a6ee-1
- Update to latest snapshot.

* Thu Sep 19 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.6+git190919.173750.0d91e560-1
- Update to latest snapshot.

* Tue Sep 17 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.6+git190917.211236.5f6db296-1
- Update to latest snapshot.

* Sat Sep 14 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.6+git190914.122325.c1e47b35-1
- Update to latest snapshot.

* Sun Sep 08 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.6+git190908.192247.6e68ce1f-1
- Update to latest snapshot.

* Mon Aug 26 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.6+git190826.042224.0daef6e9-1
- Update to latest snapshot.

* Thu Aug 22 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.6+git190822.112223.8597e028-1
- Update to latest snapshot.

* Tue Aug 20 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.6+git190820.112215.353834ed-1
- Update to latest snapshot.

* Fri Aug 16 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.6+git190816.084834.4f37489a-1
- Update to latest snapshot.

* Thu Aug 15 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.6+git190815.182207.2b2c2c08-1
- Update to latest snapshot.

* Thu Aug 15 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.6+git190815.174535.66ff4da7-1
- Update to latest snapshot.

* Tue Jul 30 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.6+git190730.152046.3c0c5e0b-1
- Update to latest snapshot.

* Sat Jul 27 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.6+git190727.225844.5c5c1b67-1
- Update to latest snapshot.

* Wed Jul 24 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.6+git190724.212555.eb28467a-1
- Update to latest snapshot.

* Sat Jul 20 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.6+git190716.164948.6fbfca49-1
- Update to version 5.3.6.

* Tue Jul 16 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.5+git190716.164948.6fbfca49-1
- Update to latest snapshot.

* Mon Jul 15 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.5+git190715.150211.8651be03-1
- Update to latest snapshot.

* Tue Jul 09 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.5+git190709.171026.c941d62c-1
- Update to latest snapshot.

* Mon Jul 01 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.5+git190701.221817.edb33fa4-1
- Update to latest snapshot.

* Thu Jun 27 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.5+git190627.204352.1940f06d-1
- Update to latest snapshot.

* Wed Jun 26 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.5+git190626.204639.37c75bfe-1
- Update to latest snapshot.

* Thu Jun 06 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.5+git190606.193019.65ad21ee-1
- Update to latest snapshot.

* Thu Jun 06 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.5+git190604.224919.a3eee4b3-1
- Update to version 5.3.5.

* Tue Jun 04 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.4+git190604.224919.a3eee4b3-1
- Update to latest snapshot.

* Fri May 31 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.4+git190531.045158.341993ab-1
- Update to latest snapshot.

* Mon Apr 15 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.4+git190415.163524.635128bd-1
- Update to latest snapshot.

* Sun Apr 14 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.4+git190414.162910.7f160d9a-1
- Update to latest snapshot.

* Mon Apr 08 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.4+git190408.055327.50037237-1
- Update to latest snapshot.

* Fri Apr 05 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.4+git190405.200325.b61cd8d7-1
- Update to latest snapshot.

* Fri Apr 05 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.4+git190405.195220.767d244b-1
- Update to latest snapshot.

* Sun Mar 31 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.4+git190331.225223.b4a611c8-1
- Update to latest snapshot.

* Sat Mar 30 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.4+git190330.225223.2de13adf-1
- Update to latest snapshot.

* Sat Mar 30 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.4+git190329.104531.3417f0d4-1
- Update to version 5.3.4.

* Fri Mar 29 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.3+git190329.104531.3417f0d4-1
- Update to latest snapshot.

* Wed Mar 13 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.3+git190313.162720.3a9900c0-1
- Update to latest snapshot.

* Tue Mar 12 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.3+git190312.152712.7cff1adf-1
- Update to latest snapshot.

* Mon Mar 11 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.3+git190311.144708.6d3b1775-1
- Update to latest snapshot.

* Fri Mar 08 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.3+git190308.181834.618cf050-1
- Update to latest snapshot.

* Tue Feb 12 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.3+git190212.000713.bf3bbcf7-1
- Update to latest snapshot.

* Mon Feb 11 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.3+git190211.132159.ee4ab201-1
- Update to latest snapshot.

* Tue Feb 05 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.3+git190205.000724.83507a9f-1
- Update to latest snapshot.

* Thu Jan 31 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.3+git190131.215930.e4dfa8c8-1
- Update to latest snapshot.

* Tue Jan 22 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.3+git190122.160427.f4c2af08-1
- Update to latest snapshot.

* Fri Jan 18 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.3+git190118.102717.0efbbec6-1
- Update to latest snapshot.

* Tue Jan 15 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.3+git190115.121638.6a51ac70-1
- Update to latest snapshot.

* Mon Jan 14 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.3+git190114.001058.c06a2d99-1
- Update to latest snapshot.

* Sat Jan 12 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.3+git190112.000935.b6bc560a-1
- Update to latest snapshot.

* Fri Jan 11 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.3+git190111.000645.5e638378-1
- Update to latest snapshot.

* Sun Jan 06 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.3+git190106.115921.1d243645-1
- Update to latest snapshot.

* Sat Jan 05 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.3+git190105.032712.13d35311-1
- Update to latest snapshot.

* Wed Jan 02 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.3+git190102.220839.3e70c1a4-1
- Update to latest snapshot.

* Tue Jan 01 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.3+git190101.003642.6c53ebf2-1
- Update to latest snapshot.

* Sun Dec 30 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.3+git181230.000431.23d6f40a-1
- Update to latest snapshot.

* Mon Dec 24 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.3+git181224.104819.5ce4053d-1
- Update to latest snapshot.

* Mon Dec 24 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.3+git181224.000729.84fbc8d5-1
- Update to latest snapshot.

* Fri Dec 21 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.3+git181221.000113.907ec3d8-1
- Update to latest snapshot.

* Tue Dec 18 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.3+git181218.104203.26b805a7-1
- Update to version 5.3.3.

* Tue Dec 18 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181218.104203.26b805a7-1
- Update to latest snapshot.

* Mon Dec 17 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181217.105335.73d5edb7-1
- Update to latest snapshot.

* Sun Dec 16 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181216.192915.9dc906a3-1
- Update to latest snapshot.

* Thu Dec 13 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181213.140727.b34a29ab-1
- Update to latest snapshot.

* Thu Dec 13 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181212.230217.5a2ffdf8-1
- Update to latest snapshot.

* Wed Dec 12 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181212.050801.b3a35eeb-1
- Update to latest snapshot.

* Wed Dec 12 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181212.001128.19b891f4-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181211.211349.b65c1ff5-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181211.190943.441c7a87-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181211.173915.64fe7a34-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181211.145409.a56af4b6-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181211.121511.9758b479-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181211.110511.d962cec3-1
- Update to latest snapshot.

* Mon Dec 10 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181210.171530.bf5734da-1
- Update to latest snapshot.

* Fri Dec 07 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181206.230431.8787324b-1
- Update to latest snapshot.

* Thu Dec 06 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181206.225714.a7964354-1
- Update to latest snapshot.

* Wed Dec 05 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181205.190514.0dc43a8a-1
- Update to latest snapshot.

* Wed Dec 05 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181204.233619.8108c284-1
- Update to latest snapshot.

* Tue Dec 04 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181204.180347.2b15d81f-1
- Update to latest snapshot.

* Tue Dec 04 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181204.173820.5abbbe35-1
- Update to latest snapshot.

* Mon Dec 03 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181203.210139.4328ae71-1
- Update to latest snapshot.

* Mon Dec 03 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181203.170452.b284d81c-1
- Update to latest snapshot.

* Sun Dec 02 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181202.201317.81f5e81f-1
- Update to latest snapshot.

* Wed Nov 28 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181128.054633.93b3e65f-1
- Update to latest snapshot.

* Tue Nov 27 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181127.170504.f2d6936b-1
- Update to latest snapshot.

* Tue Nov 27 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181127.165134.63543362-1
- Update to latest snapshot.

* Tue Nov 27 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181127.010155.deb2bdab-1
- Update to latest snapshot.

* Mon Nov 26 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181126.210823.c105eb5e-1
- Update to latest snapshot.

* Mon Nov 26 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181126.162152.23d29d2a-1
- Update to latest snapshot.

* Fri Nov 23 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181123.135902.3ad095c6-1
- Update to latest snapshot.

* Fri Nov 23 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181123.100348.a7e9aafd-1
- Update to latest snapshot.

* Fri Nov 23 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181123.094607.781705a7-1
- Update to latest snapshot.

* Fri Nov 23 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181123.060406.92d13e44-1
- Update to latest snapshot.

* Fri Nov 23 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181123.003434.be6e7e0d-1
- Update to latest snapshot.

* Thu Nov 22 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181122.211024.abe5f7b9-1
- Update to latest snapshot.

* Thu Nov 22 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181122.202455.e56ca061-1
- Update to latest snapshot.

* Wed Nov 21 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181121.094355.1acace71-1
- Update to latest snapshot.

* Sat Nov 17 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181117.005252.5a3a1126-1
- Update to latest snapshot.

* Fri Nov 16 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181116.212616.d854d85f-1
- Update to latest snapshot.

* Fri Nov 16 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181116.195602.61ce8bec-1
- Update to latest snapshot.

* Thu Nov 15 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181115.182756.281a8f96-1
- Update to latest snapshot.

* Wed Nov 14 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181114.134203.f1b13196-1
- Update to latest snapshot.

* Mon Nov 12 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181112.010405.679964d5-1
- Update to latest snapshot.

* Sat Nov 10 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181110.184702.10b412aa-1
- Update to latest snapshot.

* Fri Nov 09 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181109.165127.fdd55323-1
- Update to latest snapshot.

* Fri Nov 09 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181109.152032.e24f85f2-1
- Update to latest snapshot.

* Fri Nov 09 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181109.131102.1fd4a9fb-1
- Update to latest snapshot.

* Fri Nov 09 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181109.073649.3a2eadda-1
- Update to latest snapshot.

* Fri Nov 09 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181108.231154.8285aeda-1
- Update to latest snapshot.

* Thu Nov 08 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181108.145201.32cea791-1
- Update to latest snapshot.

* Thu Nov 08 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181108.093515.c1713a6a-1
- Update to latest snapshot.

* Thu Nov 08 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181108.082456.9faf218f-1
- Update to latest snapshot.

* Thu Nov 08 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181108.072433.951d587b-1
- Update to latest snapshot.

* Thu Nov 08 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181108.031628.36240856-1
- Update to latest snapshot.

* Thu Nov 08 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181107.230624.99afceef-1
- Update to latest snapshot.

* Tue Nov 06 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181105.211508.cad64da0-2
- Require granite 5.2.0.

* Mon Nov 05 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181105.211508.cad64da0-1
- Update to latest snapshot.

* Sat Nov 03 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181103.220721.e89db004-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181030.104807.5c184252-2
- Occasional mass rebuild.

* Tue Oct 30 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2+git181030.104807.5c184252-1
- Update to version 5.3.2.

* Tue Oct 30 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.1+git181030.104807.5c184252-1
- Update to latest snapshot.

* Mon Oct 29 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.1+git181029.172707.4bcb6599-1
- Update to latest snapshot.

* Mon Oct 29 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.1+git181029.101022.31fc6757-1
- Update to latest snapshot.

* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.1+git181025.201648.17f163d8-1
- Update to latest snapshot.

* Mon Oct 22 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.1+git181022.162932.746b610e-1
- Update to latest snapshot.

* Mon Oct 22 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.1+git181022.152758.cb1c88b8-1
- Update to latest snapshot.

* Fri Oct 19 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.1+git181019.184058.b5539e00-1
- Update to latest snapshot.

* Fri Oct 19 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.1+git181018.193732.1691835e-1
- Update to version 5.3.1.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.3+git181018.193732.1691835e-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.3+git181016.073905.f39dd203-1
- Update to latest snapshot.

* Sun Oct 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.3+git181014.181819.7f043a06-1
- Update to latest snapshot.

* Sun Oct 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.3+git181014.162634.63acba71-1
- Update to latest snapshot.

* Sun Oct 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.3+git181014.000414.cfe8b33e-1
- Update to latest snapshot.

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.3+git181013.221937.e39090bf-1
- Update to latest snapshot.

* Thu Oct 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.3+git181011.110008.8c355e22-1
- Update to latest snapshot.

* Wed Oct 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.3+git181010.185241.70ea6680-1
- Update to latest snapshot.

* Wed Oct 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.3+git181010.175007.55d46275-1
- Update to latest snapshot.

* Wed Oct 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.3+git181010.000238.5a2d3986-1
- Update to latest snapshot.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.3+git181009.072845.c5a28497-1
- Update to latest snapshot.

* Sun Oct 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.3+git181007.024024.daba9e34-1
- Update to latest snapshot.

* Thu Oct 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.3+git180926.210607.f051fd58-1
- Update to version 0.5.3.

* Wed Sep 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.2+git180926.210607.f051fd58-1
- Update to latest snapshot.

* Tue Sep 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.2+git180925.000300.69419aff-1
- Update to latest snapshot.

* Thu Sep 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.2+git180920.000520.6dba0a84-1
- Update to latest snapshot.

* Fri Sep 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.2+git180907.000104.45dc761e-1
- Update to latest snapshot.

* Thu Sep 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.2+git180906.133342.9a7c9d3b-1
- Update to latest snapshot.

* Thu Sep 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.2+git180906.040843.c784859b-1
- Update to latest snapshot.

* Thu Aug 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.2+git180830.000331.81a27816-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.2+git180829.164859.7e332967-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.2+git180829.071635.3368a1fd-1
- Update to latest snapshot.

* Mon Aug 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.2+git180825.151204.28f2bf47-1
- Update to version 0.5.2.

* Mon Aug 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.1+git180825.151204.28f2bf47-1
- Update to latest snapshot.

* Thu Aug 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.1+git180822.223243.ba8bc682-1
- Update to latest snapshot.

* Tue Aug 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.1+git180821.000036.87a48494-2
- Adapt to upstream build system changes.

* Tue Aug 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.1+git180821.000036.87a48494-1
- Update to latest snapshot.

* Mon Aug 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.1+git180820.211453.914d4b0e-1
- Update to latest snapshot.

* Mon Aug 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.1+git180820.154603.0ebbc826-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.1+git180813.000415.e13ae452-2
- Occasional mass rebuild.

* Mon Aug 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.1+git180813.000415.e13ae452-1
- Update to latest snapshot.

* Wed Aug 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.1+git180808.000159.d7e1759d-1
- Update to latest snapshot.

* Sun Aug 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.1+git180805.015233.cb452e38-1
- Update to latest snapshot.

* Fri Aug 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.1+git180803.000446.5ddcb4a2-1
- Update to version 0.5.1.

* Tue Jul 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5+git180724.000553.3b0e7c55-1
- Update to latest snapshot.

* Mon Jul 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5+git180723.200114.c690a5d0-1
- Update to latest snapshot.

* Sun Jul 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5+git180722.000409.6ffd8690-1
- Update to latest snapshot.

* Fri Jul 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5+git180713.000431.94ab9926-1
- Update to latest snapshot.

* Sat Jul 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5+git180704.210958.109c3687-2
- Remove upstreamed patch.

* Fri Jul 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5+git180704.210958.109c3687-1
- Update to version 0.5.

* Thu Jul 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180704.210958.109c3687-1
- Update to latest snapshot.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180702.000719.0f671358-1
- Update to latest snapshot.

* Fri Jun 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180615.000055.7ed6b95e-1
- Update to latest snapshot.

* Thu Jun 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180614.140956.36f25833-1
- Update to latest snapshot.

* Thu Jun 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180614.000949.30b7804b-1
- Update to latest snapshot.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180613.165033.dee5f425-1
- Update to latest snapshot.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180613.000822.b518b53a-1
- Update to latest snapshot.

* Mon Jun 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180611.191933.c6ab21ae-1
- Update to latest snapshot.

* Sat Jun 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180609.185107.be519fd0-1
- Update to latest snapshot.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180608.000436.be57f35a-1
- Update to latest snapshot.

* Thu Jun 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180607.183554.273207ca-1
- Update to latest snapshot.

* Thu Jun 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180607.170251.04918678-1
- Update to latest snapshot.

* Thu Jun 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180607.073655.8cf541b5-1
- Update to latest snapshot.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180606.154219.fd6b6e9d-1
- Update to latest snapshot.

* Tue Jun 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180605.145844.f46b9eee-1
- Update to latest snapshot.

* Sun Jun 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180603.062108.557d03d6-1
- Update to latest snapshot.

* Sat Jun 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180602.000729.30b50270-1
- Update to latest snapshot.

* Fri Jun 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180601.000206.672051b5-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180531.074035.44abbfe9-1
- Update to latest snapshot.

* Tue May 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180529.122627.f556ea8a-1
- Update to latest snapshot.

* Sat May 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180526.000218.3f843636-1
- Update to latest snapshot.

* Thu May 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180519.001116.44ba2775-1
- Update to latest snapshot.

* Mon May 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180514.074915.30343fbb-2
- Adapt to added fish shell support.

* Mon May 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180514.074915.30343fbb-1
- Update to latest snapshot.

* Sat May 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180512.000259.bc0ce90e-1
- Update to latest snapshot.

* Fri May 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180511.120458.f9de1e0a-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180510.172217.147e2be2-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180510.000945.f3f40bf4-1
- Update to latest snapshot.

* Sun May 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180506.001041.2b05dd96-1
- Update to latest snapshot.

* Thu May 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180503.175642.cfe448c3-1
- Update to latest snapshot.

* Thu May 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180503.000646.14f48f71-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180501.170605.75b30164-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180429.145241.53a15da1-2
- Add patch to fix build with vte291 >= 0.52.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180429.145241.53a15da1-1
- Update to latest snapshot.

* Thu Apr 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180426.000423.ea72c75e-1
- Update to latest snapshot.

* Wed Apr 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180425.171107.8c152b2b-1
- Update to latest snapshot.

* Wed Apr 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180425.000409.69339805-1
- Update to latest snapshot.

* Mon Apr 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180423.001008.7223e0ce-1
- Update to latest snapshot.

* Fri Apr 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180420.000932.f36b88ce-1
- Update to latest snapshot.

* Thu Apr 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180419.185804.b5486ac5-1
- Update to latest snapshot.

* Sun Apr 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180406.191202.fdce14a3-1
- Update to latest snapshot.

* Thu Apr 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180405.170708.de281e67-1
- Update to latest snapshot.

* Wed Apr 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180404.000739.d4a64e09-1
- Update to latest snapshot.

* Tue Apr 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180402.104647.3e83a238-1
- Update to latest snapshot.

* Tue Mar 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180327.000243.25f359a4-1
- Update to latest snapshot.

* Mon Mar 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180326.184645.1caed1b5-1
- Update to latest snapshot.

* Mon Mar 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180326.073737.e9716bb7-1
- Update to latest snapshot.

* Sun Mar 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180324.000901.5019eba8-1
- Update to latest snapshot.

* Thu Mar 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180322.072813.842d71c7-2
- Adapt to CMake -> meson switch.

* Thu Mar 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180322.072813.842d71c7-1
- Update to latest snapshot.

* Tue Mar 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180320.001225.3ab5070f-1
- Update to latest snapshot.

* Sun Mar 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180318.000840.054d9f96-1
- Update to latest snapshot.

* Thu Mar 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180315.002008.9721926d-1
- Update to latest snapshot.

* Mon Mar 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180312.000038.f1d0c360-1
- Update to latest snapshot.

* Sun Mar 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180311.195045.f3c04f27-1
- Update to latest snapshot.

* Sat Mar 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180310.000131.b0e35828-1
- Update to latest snapshot.

* Fri Mar 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180309.000630.74e54179-1
- Update to latest snapshot.

* Mon Mar 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180302.221644.3b8766b5-1
- Update to latest snapshot.

* Sun Feb 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180218.060652.aa90bee7-1
- Update to latest snapshot.

* Wed Feb 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180214.022835.176bd1a7-1
- Update to latest snapshot.

* Tue Feb 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180213.201510.d0d55529-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180211.000933.6107e806-1
- Update to latest snapshot.

* Thu Feb 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180201.162050.9e248fab-1
- Update to latest snapshot.

* Mon Jan 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180129.000256.4a45e09f-1
- Update to latest snapshot.

* Sun Jan 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180128.000905.806d3405-1
- Update to latest snapshot.

* Fri Jan 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180126.000933.5f8c2254-1
- Update to latest snapshot.

* Thu Jan 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180125.173350.1f3903cc-1
- Update to latest snapshot.

* Sat Jan 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180120.220929.04c0e4ff-1
- Update to latest snapshot.

* Sat Jan 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180120.153501.655d7c98-1
- Update to latest snapshot.

* Sat Jan 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180120.140456.e4a415ff-1
- Update to latest snapshot.

* Sat Jan 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180120.132931.8c2a36d0-1
- Update to latest snapshot.

* Fri Jan 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180119.223652.2620de17-1
- Update to latest snapshot.

* Thu Jan 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180118.161816.e77ad0fb-1
- Update to latest snapshot.

* Mon Jan 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180113.171426.3c3448e4-1
- Update to latest snapshot.

* Wed Jan 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180110.111640.ce8e3d02-1
- Update to latest snapshot.

* Wed Jan 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180110.000212.fd0e5f92-2
- Adapt to upstream file changes.

* Wed Jan 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180110.000212.fd0e5f92-1
- Update to latest snapshot.

* Tue Jan 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180109.210401.2a1f43ae-1
- Update to latest snapshot.

* Wed Jan 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180103.094831.1a42c0a7-1
- Initial package.


