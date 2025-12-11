%define _topdir %{getenv:PWD}/rpmbuild
%global __brp_check_rpaths %{nil}

Name:           myune_music
Version:        0.8.0
Release:        1%{?dist}
Summary:        A music player built with Flutter
License:        Apache-2.0
URL:            https://github.com/xleave/myune_music_material
BuildArch:      x86_64

%description
Myune Music is a music player built with Flutter.

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/opt/%{name}
# Copy files from the build directory
cp -r %{getenv:PWD}/build/linux/x64/release/bundle/* %{buildroot}/opt/%{name}/

# Create executable link
mkdir -p %{buildroot}/usr/bin
ln -s /opt/%{name}/myune_music %{buildroot}/usr/bin/%{name}

# Create desktop entry
mkdir -p %{buildroot}/usr/share/applications
cat > %{buildroot}/usr/share/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=Myune Music
Exec=%{name}
Icon=/opt/%{name}/data/flutter_assets/assets/images/icon/icon.png
Type=Application
Categories=AudioVideo;Player;
Terminal=false
EOF

%files
/opt/%{name}
/usr/bin/%{name}
/usr/share/applications/%{name}.desktop

%changelog
* Wed Dec 11 2025 Max <max@example.com> - 0.8.0-1
- Initial release
