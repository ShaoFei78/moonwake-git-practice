# Contribution Guide

## 1. 基本原则

- 正式项目的 `main` 保存已经 Review、完成岸上验证并可作为下一项工作起点的代码；
- 不直接在 `main` 上开发或推送；
- 一个短期任务分支只处理一个明确目标，合并后删除；
- 所有正式修改通过 Pull Request 进入上游仓库；
- 作者不自行合并自己的 PR；
- 不建立长期 `dev` 或 `debug` 分支。

本仓库是一个可重复使用的协作练习基线，因此 `main` 会保留未完成的几何计算函数。实现这些函数的练习 PR 在完成 Review 后关闭而不合并，以保证后续贡献者获得相同的起始状态。文档、测试基础设施等仓库维护修改是否合并，由 Maintainer 单独判断。

## 2. Fork 工作流

个人 Fork 使用 `origin`，战队正式仓库使用 `upstream`。

```text
upstream/main
     │ Fork
     ▼
origin/main
     │ Clone
     ▼
本地 main → 任务分支 → origin/任务分支 → PR → upstream/main
```

开始任务前同步最新 `upstream/main`，再创建任务分支。收到 Review 后继续更新原分支和原 PR。合并后同步 `main`，删除已完成分支。

普通 PR 目标是 `upstream/main`。只有 Maintainer 明确要求时，才把 PR 提交到 `integration/*` 或 `release/*`。

## 3. 分支命名

统一格式：

```text
<type>/<scope>-<short-description>
```

使用小写英文和连字符，不使用空格、中文、人名或 `final`。

示例：

```text
feat/perception-buoy-tracking
fix/camera-frame-timeout
docs/ros2-add-camera-guide
feat/42-perception-buoy-tracking
```

允许的类型：`feat`、`fix`、`hotfix`、`refactor`、`test`、`docs`、`chore`、`experiment`。

固定 scope：`camera`、`perception`、`localization`、`fusion`、`planning`、`navigation`、`ros2`、`deploy`、`tools`、`docs`。

`hotfix/*`、`integration/*` 和 `release/*` 由 Maintainer 按实际工作安排，普通贡献者不自行创建。

## 4. Commit

提交前检查：

```bash
git status
git diff
git add <明确的文件路径>
git diff --staged
```

Commit 信息遵循 Conventional Commits：

```text
<type>(可选 scope): 简短描述
```

示例：

```text
docs(ros2): add camera launch guide
fix(camera): handle empty frames
feat(perception): add red buoy filtering
```

常用类型为 `feat`、`fix`、`docs`、`refactor`、`test`、`build`、`ci` 和 `chore`。不要使用 `update`、`finish`、“改了一下”或“最终版本”等无法说明修改目的的信息。

## 5. 如何写好一个 Pull Request

创建 PR 前确认：

- Base repository 是战队上游仓库；
- Base branch 通常是 `main`；
- Head repository 是个人 Fork；
- Compare branch 是当前任务分支；
- PR 只包含当前任务所需的修改；
- PR 标题符合 Conventional Commits；
- 已写明目标、主要修改、验证方法与实际结果、风险和限制。

工作尚未完成但需要提前讨论时，可以创建 Draft PR。Draft 不能合并，仍应写清已完成内容、剩余工作、希望讨论的部分和待执行测试。准备完成后再标记为 Ready for review。

正式项目中的普通任务 PR 默认使用 Squash and merge，作者不得自行合并。本仓库中用于实现保留 TODO 的练习 PR 完成 Review 后关闭，不合并到 `main`。

## 6. Review

Review 应指出具体位置、原因和可执行建议。必须修改的问题使用 Request changes；确认可以合并时使用 Approve；仅代表偏好的非阻塞意见可标记为 `nit:`。

作者完成修改后，在原分支继续 Commit 和 Push，并在原 PR 回复处理方式。不要为了回应 Review 重新创建 PR。

## 7. 文件与安全

不要提交：

- 密钥、Token、密码、SSH 私钥和真实 `.env`；
- 数据集、模型权重、TensorRT Engine、rosbag 和视频；
- `build/`、`install/`、`log/`、可执行文件和缓存；
- 只适用于个人电脑的配置。

不要粗暴忽略全部 YAML；正式 ROS 2 参数和团队配置通常应纳入版本管理。

在不了解影响时，不要自行使用：

```text
git reset --hard
git push --force
rm -rf .git
```

求助时保留当前目标、所在分支、完整命令和报错、`git status` 与 `git remote -v`。发送前检查输出中是否包含秘密。

## 8. Tag 提醒

真实上船或下水验证通过后，由 Maintainer 在实际使用的 Commit 上创建 annotated tag：

```text
onboard-YYYYMMDD-NN
```

正式软件发布使用 `vX.Y.Z`。已发布 Tag 不移动、不复用，普通贡献者不自行创建 Tag。
