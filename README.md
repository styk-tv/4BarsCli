[![PyPI version](https://badge.fury.io/py/fourbars.svg)](https://badge.fury.io/py/fourbars) [![TravisCI](https://api.travis-ci.com/styk-tv/4bars.svg)](https://travis-ci.com/styk-tv/4bars)


# 4bars by MusicAsCode
In Ableton Live, automatically record 4 bar sequences. Multi-scene record, then export all new recordings, name them, catalogue them.

## Ableton Workflow as Code
- inject several midi tracks (as code)
- setup devices (as code)
- configure devices (program, controls)
- apply envelopes to clips
- export as 4 bars audio
- use track+clip+RandomName+index naming conventions and output files to destination folder
- (optional) submit 4 bar sequences to 4bars.media for social sequencing

## Requirements
- Ableton Live v10.1+
- python 3.7.2 +
- brew install ffmpeg
- pyenv vritualenv 4bars (you will need pyenv virtualenv with 3.7.2 named 4bars)
- brew install liblo 
- [pylive](https://github.com/ideoforms/pylive) (freedom to work with Live outside of Live python)
- liveosc (forked for AL10+, comes with pylive)
- ClyphX Pro (commercial version)
- sendmidi receivemidi (for stubborn program changes of vst devices)
- gzip (for extracting of ableton project files)
- Mac OS X (not tested on any other platform at the moment)

## Installation

Currently, based way to install 4bars is by cloning this repo.

- clone 
- run install_mac.sh
- run pip install -r requirements.txt
- ableton midiscript: ClyphX Pro installed and selected as active Control Surface in Preferences/Link Midi
- ableton midiscript: LiveOSC (fork maintained by pylive guys) installed and selected as active Control Surface in Preferences/Link Midi 

pip package called `fourbars` is currently WIP and will be published by TravisCI on every merge to master.

## Usage

After installation you should be able to type `4bars` form anywhere in your cli.
List of commands will appear:

```$xslt
Usage: 4bars (BETA) [-version] [-help] <command> [args]

The available commands for execution are listed below
Commands marked [WIP] are work-in-progress

Common commands:
    cd          essential directory navigation
    set         set management
    track       current track setup
    device      [WIP] device management
    record      [WIP] record all clips on 4BARS_ prefixed track
    sync        [WIP] synchronize exported assets with 4bars.media
    status      check if all requirements and communication is working
    login       [WIP] login to 4bars service. obtain api token
```
## Release History

- 1.0.1 - 2019.09.26 - Initial CLI release with multilevel arguments and basic Live connectivity

## Roadmap for version 1.5

Immediate roadmap and to do list is to be able to initialize new Ableton project file then inject ClyphX control track and "play" ClyphX clips in various configuration to constuct a workspace for loop recording. One one side you will end up with a Track or a TrackGroup with midi files, then device setup and then upon of execution a cascading recording will initiate to record each clip and essentially convert it from MIDI, through a device (VST synth and VST plugins) to record track. Just to give you an example. Injection of 20 midi files, setup of devices, creating of recording session for each of the clips will take one 4bars command and few seconds of Ableton Live executing a UI sequence. 

All recorded clips will be then collected from Recordings folder through discovery in Ableton project file and placed in 4bars local directory structure. A renaming convention will be applied based on Track/Clip names. Name generator can optionally be used based on world list from randomnames package so you will end up with AdjectiveNoun pairs for easy reference. Commands will be added to 4bars to make this trivial.

Default ffmpeg LAME encoder for MP3 adds a 25ms silence on both pre-loop and post-loop essentially making MP3s useless for the looping purposes. Local preconfigured ffmpeg can then be triggered to perform mass conversions from ALS (full quality 48Khz) to OGG/AAC 48khz pairs at both (96kbs/s and 320kbps/s). Having OGG/ACC pairs allows for full coverage of browser HTML5 playbecks. Commands will be added to 4bars to make this trivial. Take a look at table below.

```$xslt
     <audio controls="controls">
         <source src="loop.aac" type="audio/aac" />
     </audio>

     +---------------------+-----+-----+
     | Browser             | Ogg | AAC |
     +---------------------+-----+-----+
     | Internet Explorer   | No  | Yes |
     | Firefox             | Yes | No  |
     | Chrome              | Yes | Yes |
     | Safari              | No  | Yes |
     | Opera               | Yes | No  |
     +---------------------+-----+-----+
```

Local files, can then be mass tagged and uploaded to `4bars.media` online space for social sequencing purposes and further distribution as required.

## Help
* Join "MusicAsCode" @ [Slack Invite](https://join.slack.com/t/musicascode/shared_invite/zt-dchgrsqu-DpZZ4ccIY68qMCONXOzH7g)
* Join "MusicAsCode" @ [Discord Invite](https://discord.gg/3ve6Ue6)
