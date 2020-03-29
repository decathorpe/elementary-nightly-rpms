%global __provides_exclude_from ^%{_libdir}/(switchboard)/.*\\.so$

%global plug_type network
%global plug_name online-accounts
%global plug_rdnn io.elementary.switchboard.onlineaccounts

Name:           switchboard-plug-onlineaccounts
Summary:        Switchboard Online Accounts plug
Version:        2.0.1+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv2

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite) >= 0.5
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libaccounts-glib)
BuildRequires:  pkgconfig(libsignon-glib) >= 2.0
BuildRequires:  pkgconfig(rest-0.7)
BuildRequires:  pkgconfig(switchboard-2.0)
BuildRequires:  pkgconfig(webkit2gtk-4.0)

Requires:       switchboard%{?_isa}
Supplements:    switchboard%{?_isa}

Requires:       hicolor-icon-theme

# make sure old sub-packages are removed upon upgrade
Provides:       pantheon-online-accounts
Obsoletes:      pantheon-online-accounts

Provides:       pantheon-online-accounts-libs
Obsoletes:      pantheon-online-accounts-libs

Obsoletes:      pantheon-online-accounts-devel


%description
%{summary}.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{plug_name}-plug


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{plug_rdnn}.appdata.xml


%files -f %{plug_name}-plug.lang
%{_libdir}/switchboard/%{plug_type}/lib%{plug_name}.so

%{_libexecdir}/io.elementary.online-accounts.*

%{_datadir}/accounts/providers/*.provider
%{_datadir}/accounts/services/*.service
%{_datadir}/dbus-1/services/com.google.code.AccountsSSO.gSingleSignOnUI.service
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_datadir}/metainfo/%{plug_rdnn}.appdata.xml


%changelog
* Sun Mar 29 2020 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git200329.210955.b3c67c65-1
- Update to latest snapshot.

* Fri Mar 27 2020 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git200327.190951.ffcdbb9d-1
- Update to latest snapshot.

* Tue Mar 24 2020 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git200324.180945.05b41fa3-1
- Update to latest snapshot.

* Sun Mar 22 2020 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git200322.010942.0c1cccfb-1
- Update to latest snapshot.

* Thu Mar 19 2020 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git200319.190945.b6f8cbdf-1
- Update to latest snapshot.

* Tue Mar 17 2020 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git200317.180934.da1d480d-1
- Update to latest snapshot.

* Mon Mar 16 2020 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git200316.120933.800e4c27-1
- Update to latest snapshot.

* Fri Mar 13 2020 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git200313.221633.c687b9a5-1
- Update to latest snapshot.

* Fri Mar 13 2020 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git200313.184049.40278335-1
- Update to latest snapshot.

* Fri Mar 13 2020 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git200312.232630.c0d42a7b-1
- Update to latest snapshot.

* Thu Mar 12 2020 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git200312.203235.bf560400-1
- Update to latest snapshot.

* Sun Mar 01 2020 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git200301.150931.fa0eb87c-1
- Update to latest snapshot.

* Sat Feb 22 2020 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git200222.140903.2f524673-1
- Update to latest snapshot.

* Thu Feb 06 2020 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git200206.200829.d8da4cd3-1
- Update to latest snapshot.

* Sat Feb 01 2020 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git200201.020826.7edc9d62-1
- Update to latest snapshot.

* Wed Jan 29 2020 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git200129.180815.bc1a458b-1
- Update to latest snapshot.

* Sat Jan 25 2020 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git200125.150819.df2ca399-1
- Update to latest snapshot.

* Thu Jan 23 2020 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git200123.081001.34164a9f-1
- Update to latest snapshot.

* Thu Jan 16 2020 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git200116.020753.fe150409-1
- Update to latest snapshot.

* Sat Jan 04 2020 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git200104.110735.802331bf-1
- Update to latest snapshot.

* Thu Jan 02 2020 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git200101.230833.6f10230e-1
- Update to latest snapshot.

* Fri Dec 20 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git191220.160918.b8216d72-1
- Update to latest snapshot.

* Wed Dec 18 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git191218.175535.3d48d78c-1
- Update to latest snapshot.

* Tue Dec 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git191217.200145.4bd4f682-1
- Update to latest snapshot.

* Tue Dec 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git191217.200031.1df3197b-1
- Update to latest snapshot.

* Tue Dec 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git191217.022503.949eb94e-1
- Update to latest snapshot.

* Wed Dec 04 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git191204.212549.6c2908bd-1
- Update to latest snapshot.

* Fri Nov 22 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git191122.032512.edc41dc2-1
- Update to latest snapshot.

* Sun Nov 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git191117.202450.2a9b9d64-1
- Update to latest snapshot.

* Sat Nov 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git191116.172446.3924a5cb-1
- Update to latest snapshot.

* Fri Nov 15 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git191115.130737.55b41b13-1
- Update to latest snapshot.

* Sun Nov 10 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git191110.192436.15153b36-1
- Update to latest snapshot.

* Sat Nov 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git191109.122450.42f1bb11-1
- Update to latest snapshot.

* Wed Nov 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git191106.223832.d594b7a3-1
- Update to latest snapshot.

* Wed Nov 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git191106.175844.08161f7c-1
- Update to latest snapshot.

* Wed Nov 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git191106.164817.78d2a134-1
- Update to latest snapshot.

* Wed Oct 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git191016.202406.e5bf18a9-1
- Update to latest snapshot.

* Mon Oct 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git191014.112351.58135409-1
- Update to latest snapshot.

* Wed Oct 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git191009.172352.823318f5-1
- Update to latest snapshot.

* Mon Oct 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git191007.152356.50266def-1
- Update to latest snapshot.

* Sat Oct 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git191005.122346.05bade4c-1
- Update to latest snapshot.

* Thu Oct 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git191003.145716.1c19c0f6-1
- Update to latest snapshot.

* Wed Oct 02 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190930.142343.9db327b8-1
- Update to latest snapshot.

* Thu Sep 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190926.224033.5bcd1654-1
- Update to latest snapshot.

* Tue Sep 24 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190924.200918.71893d4e-1
- Update to latest snapshot.

* Fri Sep 20 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190920.042315.5574e016-1
- Update to latest snapshot.

* Wed Sep 18 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190918.122307.e4d96aec-1
- Update to latest snapshot.

* Tue Sep 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190917.092320.6ca6a2b0-1
- Update to latest snapshot.

* Thu Sep 12 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190912.142310.d60516f2-1
- Update to latest snapshot.

* Wed Sep 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190911.180950.d766ef23-1
- Update to latest snapshot.

* Thu Sep 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190905.192243.373e63ed-1
- Update to latest snapshot.

* Mon Aug 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190826.062241.ee070612-1
- Update to latest snapshot.

* Fri Aug 23 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190823.215207.a5c88f0a-1
- Update to latest snapshot.

* Thu Aug 15 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190814.084507.5735d128-2
- Add appdata file and validation.

* Wed Aug 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190814.084507.5735d128-1
- Update to latest snapshot.

* Tue Aug 13 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190813.153318.9f5364ec-1
- Update to latest snapshot.

* Wed Aug 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190807.152601.f7d95e38-1
- Update to latest snapshot.

* Wed Aug 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190807.042200.52010fa3-1
- Update to latest snapshot.

* Thu Aug 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190731.234638.15e52df7-1
- Update to latest snapshot.

* Wed Jul 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190717.140329.9eefff81-1
- Update to latest snapshot.

* Wed Jun 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190626.211202.7dba758d-1
- Update to latest snapshot.

* Tue Apr 30 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190430.165702.75586db0-1
- Update to latest snapshot.

* Tue Apr 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190416.092557.dc5442ce-1
- Update to latest snapshot.

* Thu Apr 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190411.215336.734e3a27-1
- Update to latest snapshot.

* Mon Apr 08 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190408.195328.d6bf13f5-1
- Update to latest snapshot.

* Mon Mar 18 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190318.135502.5fa2882f-1
- Update to latest snapshot.

* Sat Feb 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190209.105458.96c57ced-1
- Update to latest snapshot.

* Fri Feb 08 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190208.054252.8139d2ff-1
- Update to latest snapshot.

* Thu Feb 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190207.000643.6c4edb77-1
- Update to latest snapshot.

* Wed Feb 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190206.185103.e3b1eb66-1
- Update to latest snapshot.

* Sun Feb 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190203.120653.29ba3881-1
- Update to latest snapshot.

* Mon Jan 28 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190128.080943.db15183e-1
- Update to latest snapshot.

* Mon Jan 28 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190128.000615.9b46011e-1
- Update to latest snapshot.

* Sun Jan 27 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190127.000127.776421f0-1
- Update to latest snapshot.

* Fri Jan 18 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190118.050050.3fc9e8dc-1
- Update to latest snapshot.

* Tue Jan 15 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190115.000638.54548133-1
- Update to latest snapshot.

* Mon Jan 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190114.163355.110e9947-1
- Update to latest snapshot.

* Mon Jan 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190114.132419.d70f20a4-1
- Update to latest snapshot.

* Mon Jan 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190114.001039.780dfb15-1
- Update to latest snapshot.

* Sun Jan 13 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190113.090130.feb6315c-1
- Update to latest snapshot.

* Sat Jan 12 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190112.134231.8c24439e-1
- Update to latest snapshot.

* Sat Jan 12 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190112.000930.7555835a-1
- Update to latest snapshot.

* Fri Jan 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190111.205445.455ba6a5-1
- Update to latest snapshot.

* Fri Jan 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190111.131221.565cf56f-1
- Update to latest snapshot.

* Fri Jan 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190111.125152.ee458c58-1
- Update to latest snapshot.

* Fri Jan 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190111.102734.9104e2a3-1
- Update to latest snapshot.

* Fri Jan 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190111.093122.9e498b5d-1
- Update to latest snapshot.

* Fri Jan 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190111.021409.fd66be52-1
- Update to latest snapshot.

* Fri Jan 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190111.000639.b04fe07b-1
- Update to latest snapshot.

* Sun Jan 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190106.151141.43af5d48-1
- Update to latest snapshot.

* Fri Jan 04 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190104.000850.ff24a343-1
- Update to latest snapshot.

* Wed Jan 02 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190102.214549.eaa154e3-1
- Update to latest snapshot.

* Tue Jan 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git190101.004402.e6d778c2-1
- Update to latest snapshot.

* Tue Dec 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181225.000639.4afb89ea-1
- Update to latest snapshot.

* Mon Dec 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181224.000724.b2098ef8-1
- Update to latest snapshot.

* Sun Dec 23 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181223.181014.efa09ac7-1
- Update to latest snapshot.

* Sat Dec 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181222.104204.dbf3d131-1
- Update to latest snapshot.

* Fri Dec 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181221.020027.ef861b66-1
- Update to latest snapshot.

* Wed Dec 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181219.110021.ae2f42ae-1
- Update to latest snapshot.

* Mon Dec 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181217.205843.3f2c3411-1
- Update to latest snapshot.

* Mon Dec 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181217.142714.8dcd41e0-1
- Update to latest snapshot.

* Mon Dec 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181217.130317.323aebd1-1
- Update to latest snapshot.

* Mon Dec 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181217.112541.f914247a-1
- Update to latest snapshot.

* Mon Dec 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181217.105050.9471341a-1
- Update to latest snapshot.

* Mon Dec 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181217.095450.a9a849bf-1
- Update to latest snapshot.

* Mon Dec 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181217.062839.a7de59cb-1
- Update to latest snapshot.

* Sat Dec 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181214.232918.d49d9d71-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181211.064726.f63a0e05-1
- Update to latest snapshot.

* Mon Dec 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181210.221745.44028343-1
- Update to latest snapshot.

* Mon Dec 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181210.214605.49b82b64-1
- Update to latest snapshot.

* Sat Dec 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181208.214548.01987c7b-1
- Update to latest snapshot.

* Fri Dec 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181207.040301.e8aba6b3-1
- Update to latest snapshot.

* Fri Dec 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181207.025111.e212056d-1
- Update to latest snapshot.

* Sun Dec 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181202.064418.31b3e35d-1
- Update to latest snapshot.

* Mon Nov 26 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181126.071028.6e87ed56-1
- Update to latest snapshot.

* Thu Nov 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181122.064756.c58523d5-1
- Update to latest snapshot.

* Mon Nov 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181119.190442.ee602729-1
- Update to latest snapshot.

* Fri Nov 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181116.082402.6f4b520b-1
- Update to latest snapshot.

* Wed Nov 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181114.025241.2c0f038e-1
- Update to latest snapshot.

* Tue Nov 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181113.190149.cbd976ca-1
- Update to latest snapshot.

* Mon Nov 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181112.180542.a11177ca-1
- Update to latest snapshot.

* Mon Nov 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181112.170044.fb1ce336-1
- Update to latest snapshot.

* Mon Nov 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181112.154406.fe2b817a-1
- Update to latest snapshot.

* Mon Nov 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181112.050232.d9d257f0-1
- Update to latest snapshot.

* Sat Nov 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181110.161001.0f213686-1
- Update to latest snapshot.

* Sat Nov 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181110.101549.9ae0a4f2-1
- Update to latest snapshot.

* Sat Nov 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181110.071454.a16bf01e-1
- Update to latest snapshot.

* Sat Nov 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181110.025804.33a362b4-1
- Update to latest snapshot.

* Sat Nov 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181109.230142.c2972696-1
- Update to latest snapshot.

* Fri Nov 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181109.225049.525b53ed-1
- Update to latest snapshot.

* Fri Nov 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181109.190001.91195702-1
- Update to latest snapshot.

* Fri Nov 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181109.173120.97c63fef-1
- Update to latest snapshot.

* Fri Nov 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181109.063550.2d8829dc-1
- Update to latest snapshot.

* Thu Nov 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181108.210735.f9f4a764-1
- Update to latest snapshot.

* Wed Nov 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181107.165258.c192be5b-1
- Update to latest snapshot.

* Wed Nov 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181107.130735.55b07b07-1
- Update to latest snapshot.

* Tue Nov 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181106.212945.fc06b284-1
- Update to latest snapshot.

* Mon Nov 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181105.201921.0751c294-1
- Update to latest snapshot.

* Mon Nov 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181105.182101.003d6673-1
- Update to latest snapshot.

* Mon Nov 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181105.010917.6435b147-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181028.160943.facc0045-2
- Occasional mass rebuild.

* Sun Oct 28 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181028.160943.facc0045-1
- Update to latest snapshot.

* Fri Oct 26 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181025.080926.ede2d8c3-1
- Update to version 2.0.1.

* Sat Oct 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181020.133815.d4dd9bda-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181016.101331.d176a3c6-1
- Update to latest snapshot.

* Mon Oct 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181015.223557.c361131d-1
- Update to latest snapshot.

* Mon Oct 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181015.163827.3e9f8704-1
- Update to latest snapshot.

* Mon Oct 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181015.144935.58ea9191-1
- Update to latest snapshot.

* Sun Oct 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181014.021817.6d1316a4-1
- Update to latest snapshot.

* Sun Oct 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181014.000356.3d887e66-1
- Update to latest snapshot.

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181013.145651.d0792290-2
- Adapt to CMake -> meson switch.
- Adapt to upstream dependency changes.

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181013.145651.d0792290-1
- Update to latest snapshot.

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181013.123315.7186b6fe-1
- Update to latest snapshot.

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181013.082238.ddf8f687-1
- Update to latest snapshot.

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181013.010238.7509ae03-1
- Update to latest snapshot.

* Fri Oct 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181012.200027.76df4d61-1
- Update to latest snapshot.

* Fri Oct 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181012.183505.8117a332-1
- Update to latest snapshot.

* Fri Oct 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181012.163143.9563a1ba-1
- Update to latest snapshot.

* Fri Oct 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181012.122341.06b77032-1
- Update to latest snapshot.

* Thu Oct 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181010.172327.45844513-1
- Update to latest snapshot.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181009.174832.727394f4-1
- Update to latest snapshot.

* Mon Oct 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181008.000550.5148e1bb-1
- Update to latest snapshot.

* Sun Oct 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181007.024531.e16a6297-1
- Update to latest snapshot.

* Wed Oct 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181003.001112.989c409f-1
- Update to latest snapshot.

* Thu Sep 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git180920.000502.ac9f5d8b-1
- Update to latest snapshot.

* Wed Sep 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git180919.000951.4cf8463c-1
- Update to latest snapshot.

* Fri Sep 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git180907.000637.99cce44c-1
- Update to latest snapshot.

* Sat Sep 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git180901.000915.ef455438-1
- Update to latest snapshot.

* Thu Aug 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git180830.000820.31c9be9f-1
- Update to latest snapshot.

* Sun Aug 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git180819.000954.46ab224f-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git180722.121017.4d9120fe-2
- Occasional mass rebuild.

* Sun Jul 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git180722.121017.4d9120fe-1
- Update to latest snapshot.

* Sat Jul 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git180713.000426.28ab9f76-2
- Add missing BR: gcc, gcc-c++.

* Fri Jul 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git180713.000426.28ab9f76-1
- Update to latest snapshot.

* Mon Jul 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git180709.001039.065523ec-1
- Update to latest snapshot.

* Fri Jun 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git180615.001137.6681f49f-1
- Update to latest snapshot.

* Thu Jun 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git180614.084400.f7e7d699-1
- Update to latest snapshot.

* Mon Jun 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git180608.001247.71232c3e-1
- Update to version 0.3.1.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180608.001247.71232c3e-1
- Update to latest snapshot.

* Sat Jun 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180602.000659.f4a516eb-1
- Update to latest snapshot.

* Fri Jun 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180601.000846.5939f300-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180531.000340.ba846e3a-1
- Update to latest snapshot.

* Wed May 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180530.000452.f15fc437-1
- Update to latest snapshot.

* Tue May 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180529.001328.4ef48886-1
- Update to latest snapshot.

* Mon May 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180528.013226.a2d80eb8-1
- Update to latest snapshot.

* Sun May 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180527.000610.8d9f2d8a-1
- Update to latest snapshot.

* Sat May 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180525.000844.2b7afbc9-1
- Update to latest snapshot.

* Thu May 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180517.000438.7dcdfebb-1
- Update to latest snapshot.

* Wed May 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180516.142722.5a3b2494-1
- Update to latest snapshot.

* Sat May 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180512.001224.1d3bb83f-1
- Update to latest snapshot.

* Tue May 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180507.214154.8e1a7250-1
- Update to latest snapshot.

* Sun May 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180506.165017.428d765c-1
- Update to latest snapshot.

* Thu May 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180503.080142.82ff3bc0-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180429.140459.d27880a1-1
- Update to latest snapshot.

* Thu Apr 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180426.000400.bbae39f4-1
- Update to latest snapshot.

* Wed Apr 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180425.000355.fa2cf116-1
- Update to latest snapshot.

* Fri Apr 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180420.001229.076f8540-1
- Update to latest snapshot.

* Sat Apr 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180414.122720.0a67281a-1
- Update to latest snapshot.

* Sat Apr 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180413.224003.53ed4500-1
- Update to latest snapshot.

* Fri Apr 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180413.174634.57314690-1
- Update to latest snapshot.

* Wed Mar 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180328.000418.dd88920e-1
- Update to latest snapshot.

* Mon Mar 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180326.000923.e0e81d25-1
- Update to latest snapshot.

* Sun Mar 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180325.000944.f1062df8-1
- Update to latest snapshot.

* Thu Mar 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180322.000551.e076b4f0-1
- Update to latest snapshot.

* Sun Mar 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180318.000834.4ba1ddb0-1
- Update to latest snapshot.

* Wed Mar 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180314.000246.dd7645af-1
- Update to latest snapshot.

* Mon Mar 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180312.001018.6449fd0d-1
- Update to latest snapshot.

* Sat Mar 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180310.000445.baf33cb0-1
- Update to latest snapshot.

* Thu Mar 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180308.175706.fe9c5855-1
- Update to latest snapshot.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180224.000451.858c3a83-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180211.000918.86f9a2b3-1
- Update to latest snapshot.

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180205.001214.43e2b5ec-1
- Update to latest snapshot.

* Fri Jan 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180119.124731.fe7d6b39-1
- Update to latest snapshot.

* Sat Jan 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git171104.071431.369e4703-3
- Remove icon cache scriptlets.

* Thu Jan 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git171104.071431.369e4703-2
- Merge .spec file from fedora.

* Sat Nov 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git171104.071431.369e4703-1
- Update to latest snapshot.

* Sat Aug 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git170818.231615.62729c89-1
- Update to latest snapshot.

* Mon Jul 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git170703.172833.b673f979-1
- Update to latest snapshot.

* Wed Jun 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git170628.152738.cde8dcd5-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git170617.150143.919b2c92-1
- Update to latest snapshot.

* Sat Apr 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git170417.235528.5a0270aa-1
- Initial package.


