Name:           ros-indigo-multi-level-map-server
Version:        0.1.2
Release:        0%{?dist}
Summary:        ROS multi_level_map_server package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/multi_level_map_server
Source0:        %{name}-%{version}.tar.gz

Requires:       PyYAML
Requires:       python-pillow
Requires:       python-pillow-qt
Requires:       python-rospkg
Requires:       ros-indigo-multi-level-map-msgs
Requires:       ros-indigo-multi-level-map-utils
Requires:       ros-indigo-nav-msgs
Requires:       ros-indigo-rospy
Requires:       ros-indigo-tf
BuildRequires:  ros-indigo-catkin

%description
Launches a map server for various floors inside a building.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Aug 05 2015 Piyush Khandelwal <piyushk@gmail.com> - 0.1.2-0
- Autogenerated by Bloom

* Thu Mar 26 2015 Piyush Khandelwal <piyushk@gmail.com> - 0.1.1-0
- Autogenerated by Bloom

