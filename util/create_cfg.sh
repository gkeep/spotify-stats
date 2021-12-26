#!/usr/bin/env bash

bold=$(tput bold)
normal=$(tput sgr0)

if [ ! -f "$XDG_CONFIG_HOME/spotify-stats/config" ]; then
  printf "${bold}installing config...${normal}\n"
  mkdir -p "$XDG_CONFIG_HOME/spotify-stats"
  cp config.sample "$XDG_CONFIG_HOME/spotify-stats/config"
else
  printf "${bold}config is already installed.${normal}\n"
fi
