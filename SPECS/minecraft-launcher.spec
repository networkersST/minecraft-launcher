Name:           minecraft-launcher
Vendor:         Mojang AB
Version:        928
Release:        0.0.1
Summary:        Create your own world in one of the most popular video games

License:        All Rights Reserved
URL:            https://minecraft.net/
Source0:        minecraft-launcher-%{version}.tar.xz

Requires:       alsa-lib at-spi2-atk at-spi2-core atk dbus expat gdk-pixbuf2 glib2 glibc gtk3 libdrm libxcb nspr nss pango zlib

%description
Join people all over the world playing Minecraft, one of the most popular videogames around! Your own imagination is the limit in this fun game where you get to build the world around you. Play with friends, or alone, as you adventure, gather, build, and battle in an incredible land of your very own. For the best experience, we recommend you create an account and purchase online at minecraft.net/en-us/store before installing this app. ** Requires internet.
NOTE: This wrapper is not verified by, affiliated with, or supported by Mojang or Microsoft.


%prep
%setup -q

wget https://launcher.mojang.com/download/linux/x86_64/minecraft-launcher_%{version}.tar.gz
tar -xf minecraft-launcher_%{version}.tar.gz


%install

mkdir -p %{buildroot}/%{_bindir}
install -m 755 minecraft-launcher/minecraft-launcher %{buildroot}/%{_bindir}/minecraft-launcher # Executable

mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/symbolic/apps
install -m 644 minecraft-launcher.svg %{buildroot}/%{_datadir}/icons/hicolor/symbolic/apps/minecraft-launcher.svg

mkdir -p %{buildroot}/%{_datadir}/applications
install -m 644 minecraft-launcher.desktop %{buildroot}/%{_datadir}/applications/minecraft-launcher.desktop


%files
%{_bindir}/minecraft-launcher
%{_datadir}/icons/hicolor/symbolic/apps/minecraft-launcher.svg
%{_datadir}/applications/minecraft-launcher.desktop


%changelog
* Thu Nov 25 2021 Alberto Mimbrero <mimbrero.alberto@gmail.com>
- First version
