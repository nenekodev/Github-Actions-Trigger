# Github-Actions-Trigger

## Features

- Automatically starts your Github workflows **ON TIME** and **NO TIME LIMIT**
- Support cron syntax
- All the variables are imported through secrets
- Automatically deletes workflow runs that have been successfully executed
- Low memory footprint (~ 20 MB)

## System Requirements

- Python 3.6

## Usage

0. You should add 
  ```yml
  on:
    workflow_dispatch:
  ```
  to your `.github/workflows/foo.yml`.
1. Sign up and login to [Tencent Cloud SCF Console](https://console.cloud.tencent.com/scf/) 
2. Click `函数服务` which is located at left bar, Then click `新建`.
3. Click `从头开始`, select `运行环境` as `Python 3.6`. You can change your SCF name at `函数名称`.
4. Download the code from [Releases](https://github.com/nenekodev/Github-Actions-Trigger/releases), then select `提交方法` as `本地上传 zip 包`. Upload the downloaded zip by click `上传` button. Or you can copy and paste the code into the editor from `index.py`.
5. Click `高级配置`, set `初始化超时时间` to 300, set `执行超时时间` to 900.
6. Set your environment variables in `环境变量`:
  |        key       |                                                         value                                                         |
  |------------------|-----------------------------------------------------------------------------------------------------------------------|
  |   GITHUB_USER    |                                            Your username (e.g. nenekodev)                                             |
  |   GITHUB_REPO    |                                       Your repo name (e.g. asoul-wecom-notifier                                       |
  |GITHUB_ACTION_FILE|                                   Your workflow config (e.g. A-SOUL_BOT-RunOnce.yml)                                  |
  |   GITHUB_TOKEN   |Get it from [here](https://github.com/settings/tokens)<br>Name: GITHUB_TOKEN<br>Scopes: repo, workflow, admin:repo_hook|
7. Click `触发器配置`, click `自定义创建`, choose your `触发周期` or select `自定义触发周期` and type cron expression at `Cron 表达式`. Timezone is UTC +8 (Beijing, Shanghai, Chongqing, Urumuqi.
8. Then click `完成`.

## License

AGPL-3.0

