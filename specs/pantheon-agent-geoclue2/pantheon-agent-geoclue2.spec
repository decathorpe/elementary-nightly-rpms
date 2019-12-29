%global appname io.elementary.desktop.agent-geoclue2

Name:           pantheon-agent-geoclue2
Summary:        Pantheon Geoclue2 Agent
Version:        1.0.3+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3

URL:            https://github.com/elementary/pantheon-agent-geoclue2
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.34.1

BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libgeoclue-2.0)


%description
Provides a dialog asking for the user's permission when an application
requests access to location services.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang pantheon-agent-geoclue2


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f pantheon-agent-geoclue2.lang
%doc README.md
%license COPYING

%config(noreplace) %{_sysconfdir}/xdg/autostart/%{appname}-daemon.desktop

%{_libexecdir}/geoclue2-1-pantheon/

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Sun Dec 29 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.3+git191229.052120.2b6f99f4-1
- Update to latest snapshot.

* Fri Dec 27 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.3+git191227.130722.2920619e-1
- Update to latest snapshot.

* Thu Dec 26 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.3+git191226.035154.f5e71919-1
- Update to latest snapshot.

* Wed Dec 18 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.3+git191218.191208.1a1eb0f2-1
- Update to latest snapshot.

* Sun Dec 15 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.3+git191215.020708.ed23aca6-1
- Update to latest snapshot.

* Wed Dec 04 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.3+git191204.212620.5e9d7111-1
- Update to latest snapshot.

* Mon Dec 02 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.3+git191202.085754.2b27564d-1
- Update to latest snapshot.

* Thu Nov 28 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.3+git191128.162551.57dd26da-1
- Update to latest snapshot.

* Fri Nov 22 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.3+git191122.032546.e89c7a1b-1
- Update to latest snapshot.

* Sat Nov 16 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.3+git191115.232500.5cc78fdd-1
- Update to version 1.0.3.

* Sat Nov 16 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git191115.232500.5cc78fdd-1
- Update to latest snapshot.

* Fri Nov 15 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git191115.215627.c6c9cfe3-1
- Update to latest snapshot.

* Mon Nov 11 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git191111.122509.5a9e7fbe-1
- Update to latest snapshot.

* Sat Nov 09 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git191109.112444.2f8147b1-1
- Update to latest snapshot.

* Wed Nov 06 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git191106.185024.e6c9c3d2-1
- Update to latest snapshot.

* Wed Nov 06 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git191106.174020.4be7fdab-1
- Update to latest snapshot.

* Wed Nov 06 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git191106.161735.27ad8444-1
- Update to latest snapshot.

* Sat Nov 02 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git191101.232433.4cf98351-1
- Update to latest snapshot.

* Sun Oct 27 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git191027.102427.d7db686d-1
- Update to latest snapshot.

* Wed Oct 02 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git191002.160402.e80756c5-1
- Update to latest snapshot.

* Wed Oct 02 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git191002.154829.fb1c2af9-1
- Update to latest snapshot.

* Sun Sep 22 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git190922.142258.15525165-1
- Update to latest snapshot.

* Thu Sep 19 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git190919.183823.6cea250f-1
- Update to latest snapshot.

* Tue Sep 10 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git190910.172245.f9fad254-1
- Update to latest snapshot.

* Tue Aug 27 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git190827.222323.19f3722d-1
- Update to latest snapshot.

* Tue Jul 16 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git190716.201232.5a5bc355-1
- Update to latest snapshot.

* Wed Jul 03 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git190703.144025.e09b417d-1
- Update to latest snapshot.

* Sun Jun 30 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git190630.162654.84311e19-1
- Update to latest snapshot.

* Wed Jun 26 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git190626.204359.4b0093c5-1
- Update to latest snapshot.

* Wed Jun 05 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git190605.182943.81c8ca33-1
- Update to latest snapshot.

* Sat Jun 01 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git190601.111345.e3854542-1
- Update to latest snapshot.

* Fri May 31 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git190531.045058.a158da75-1
- Update to latest snapshot.

* Fri May 17 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git190517.170254.b208b3e7-1
- Update to latest snapshot.

* Sat Apr 06 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git190406.205211.0111e88e-1
- Update to latest snapshot.

* Thu Dec 20 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git181220.202735.48310f9b-1
- Update to latest snapshot.

* Thu Dec 20 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git181220.184220.a3c6c064-1
- Update to latest snapshot.

* Thu Dec 20 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git181220.170041.0c31bf0e-1
- Update to latest snapshot.

* Thu Dec 20 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git181220.075844.14695675-2
- Adapt to added appstream metadata.

* Thu Dec 20 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git181220.075844.14695675-1
- Update to latest snapshot.

* Wed Dec 19 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git181219.103359.ba28646d-1
- Update to version 1.0.1.

* Wed Dec 19 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0+git181219.103359.ba28646d-1
- Update to latest snapshot.

* Wed Dec 19 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0+git181219.093808.b5bcce79-1
- Update to latest snapshot.

* Sat Dec 01 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0+git181201.033314.341993d2-1
- Update to latest snapshot.

* Mon Nov 26 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0+git181126.000543.035047f0-1
- Update to latest snapshot.

* Sun Nov 04 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0+git181104.000321.add407dd-1
- Update to latest snapshot.

* Sat Nov 03 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0+git181103.131842.8bf08301-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0+git181025.084027.15d2a7c8-2
- Occasional mass rebuild.

* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0+git181025.084027.15d2a7c8-1
- Update to latest snapshot.

* Sun Oct 21 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0+git181021.095450.041b39f6-1
- Update to latest snapshot.

* Sat Oct 20 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0+git181020.143213.c2aaf091-1
- Update to latest snapshot.

* Fri Oct 19 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0+git181019.060935.0b8939ff-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0+git181016.022556.05b0c567-1
- Update to latest snapshot.

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0+git181013.212836.080a5a30-1
- Update to latest snapshot.

* Tue Sep 25 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0+git180925.000147.1e449f65-1
- Update to latest snapshot.

* Mon Aug 20 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0+git180820.000637.6212987d-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0+git180813.000259.1b2c4732-2
- Occasional mass rebuild.

* Mon Aug 13 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0+git180813.000259.1b2c4732-1
- Update to latest snapshot.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0+git180606.000816.c63f79a2-1
- Update to latest snapshot.

* Mon Jun 04 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0+git180604.120603.b20cc898-1
- Update to latest snapshot.

* Sun May 27 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0+git180526.080401.1effca6d-2
- Add missing dependency on gettext.

* Sun May 27 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0+git180526.080401.1effca6d-1
- Update to version 1.0.

* Sat May 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180526.080401.1effca6d-1
- Update to latest snapshot.

* Thu May 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180518.175450.80448d99-1
- Update to latest snapshot.

* Fri May 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180518.142130.a609cf74-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180510.171645.c7ccdabd-1
- Update to latest snapshot.

* Sun Mar 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180325.000904.261360f1-1
- Update to latest snapshot.

* Sat Mar 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180317.000928.5baec76b-1
- Update to latest snapshot.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180223.205534.426e0234-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180211.000811.5414fb94-1
- Update to latest snapshot.

* Sat Feb 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180203.000627.a7e6cd15-1
- Update to latest snapshot.

* Fri Feb 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180202.194401.ebdc0e5e-1
- Update to latest snapshot.

* Sat Jan 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180106.001704.829369f3-1
- Update to latest snapshot.

* Fri Dec 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git171228.234201.9e1e3292-1
- Update to latest snapshot.

* Tue Dec 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git171219.084105.b7ddc262-1
- Update to latest snapshot.

* Fri Dec 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git171215.001055.8aeda9bc-1
- Update to latest snapshot.

* Mon Jul 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git170724.025352.c25fa8d9-1
- Update to latest snapshot.

* Sun Jul 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git170702.101747.3f26f0c8-1
- Update to latest snapshot.

* Mon Jun 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git170619.135343.c7cd564f-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git170617.153024.106622e0-1
- Update to latest snapshot.

* Thu Jun 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git170607.160948.6de1e776-1
- Update to latest snapshot.

* Thu Jun 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git170531.215421.d2d45cf7-1
- Update to latest snapshot.

* Tue May 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git170529.165431.35467052-2
- Adapt to upstream file changes.

* Mon May 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git170529.165431.35467052-1
- Update to latest snapshot.

* Thu May 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git170525.031021.b0ba8ce6-1
- Update to latest snapshot.

* Wed May 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git170524.135009.054add6f-1
- Update to latest snapshot.

* Mon May 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git170430.102728.b77d163f-2
- Adapt to upstream file changes.

* Sun Apr 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git170430.102728.b77d163f-1
- Update to latest snapshot.

* Sat Apr 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git170424.172841.1b407d1b-1
- Initial package.


