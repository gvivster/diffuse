#!/usr/bin/env bash
set -euo pipefail

if ! command -v apt-get >/dev/null 2>&1; then
  echo "This script is intended for Ubuntu/Debian (apt-get not found)." >&2
  exit 1
fi

sudo apt-get update
sudo apt-get install -y \
  meson ninja-build pkg-config \
  python3 python3-gi python3-gi-cairo \
  gir1.2-gtk-3.0 libglib2.0-dev \
  gettext

if [ -d build ]; then
  meson setup --reconfigure build
else
  meson setup build
fi

meson compile -C build
sudo meson install -C build

echo "Done. Run: diffuse"
