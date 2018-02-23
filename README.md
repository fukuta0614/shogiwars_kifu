## Shogiwars_kifu

- [将棋ウォーズの棋譜検索サイト](http://swks.sakura.ne.jp/wars/kifusearch/)から棋譜をダウンロードするCLI

### Installation

    pip install git+https://github.com/fukuta0614/shogiwars_kifu.git 

### Usage

    shogiwars_kifu [-h] [-t {10,3,10s,all}] [-d SAVE_DIR] [-l] user_name

#### Options
    -h, --help              show this help message and exit
    -t {10,3,10s,all}, --game_type {10,3,10s,all}
                            game type of shogiwars
    -d SAVE_DIR, --save_dir SAVE_DIR
                            location where kifu files are downloaded
    -l, --latest            if True, only the latest kifu file will be downloaded
