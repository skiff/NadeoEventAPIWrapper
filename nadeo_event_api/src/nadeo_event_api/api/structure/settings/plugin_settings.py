from abc import ABC

from ...structure.enums import AutoStartMode


# TODO add all these settings https://doc.trackmania.com/club/competition-tool/plugin-settings/
class PluginSettings(ABC):
    def __init__(
        self,
        ad_image_urls="",
        message_timer="",
    ):
        self._ad_image_urls = ad_image_urls
        self._message_timer = message_timer

    def as_jsonable_dict(self) -> dict:
        plugin_settings = {}
        plugin_settings["S_AdImageUrls"] = self._ad_image_urls
        plugin_settings["S_MessageTimer"] = self._message_timer
        return plugin_settings


class ClassicPluginSettings(PluginSettings):
    def __init__(
        self,
        ad_image_urls="",
        message_timer="",
        auto_start_mode: AutoStartMode = AutoStartMode.DELAY,
        auto_start_delay: int = 600,
        pick_ban_start_auto: bool = False,
        pick_ban_order: str = "",
        use_auto_ready: bool = True,
        enable_ready_manager: bool = False,
        pick_ban_use_gamepad_version: bool = False,
    ):
        super().__init__(ad_image_urls=ad_image_urls, message_timer=message_timer)

        self._auto_start_mode = auto_start_mode
        self._auto_start_delay = auto_start_delay
        self._pick_ban_start_auto = pick_ban_start_auto
        self._pick_ban_order = pick_ban_order
        self._use_auto_ready = use_auto_ready
        self._enable_ready_manager = enable_ready_manager
        self._pick_ban_use_gamepad_version = pick_ban_use_gamepad_version

        self._ready_start_ratio = 1

    def as_jsonable_dict(self) -> dict:
        plugin_settings = super().as_jsonable_dict()
        plugin_settings["S_AutoStartMode"] = self._auto_start_mode.value
        plugin_settings["S_AutoStartDelay"] = self._auto_start_delay
        plugin_settings["S_PickBanStartAuto"] = self._pick_ban_start_auto
        plugin_settings["S_PickBanOrder"] = self._pick_ban_order
        plugin_settings["S_EnableReadyManager"] = self._enable_ready_manager
        plugin_settings["S_UseAutoReady"] = self._use_auto_ready
        plugin_settings["S_ReadyStartRatio"] = self._ready_start_ratio
        plugin_settings[
            "S_PickBanUseGamepadVersion"
        ] = self._pick_ban_use_gamepad_version
        return plugin_settings


class QualifierPluginSettings(PluginSettings):
    def __init__(
        self,
        ad_image_urls: str = "",
        message_timer: str = "",
        use_playlist_complete: bool = True,
    ):
        super().__init__(
            ad_image_urls=ad_image_urls,
            message_timer=message_timer,
        )

        self._use_playlist_complete = use_playlist_complete

    def as_jsonable_dict(self) -> dict:
        plugin_settings = super().as_jsonable_dict()
        plugin_settings["S_UsePlayListComplete"] = self._use_playlist_complete
        return plugin_settings


class TMWTPluginSettings(ClassicPluginSettings):
    def __init__(
        self,
        ad_image_urls="",
        message_timer="",
        auto_start_mode: AutoStartMode = AutoStartMode.DELAY,
        auto_start_delay: int = 600,
        pick_ban_start_auto: bool = True,
        pick_ban_order: str = "b:0,b:1,p:0,p:1,p:0,p:1,p:0,p:1,p:r",
        use_auto_ready: bool = True,
        ready_minimum_team_size: int = 2,
        pick_ban_use_gamepad_version: bool = True,
        enable_ready_manager: bool = True
    ):
        super().__init__(
            ad_image_urls=ad_image_urls,
            message_timer=message_timer,
            auto_start_mode=auto_start_mode,
            auto_start_delay=auto_start_delay,
            pick_ban_start_auto=pick_ban_start_auto,
            pick_ban_order=pick_ban_order,
            use_auto_ready=use_auto_ready,
            pick_ban_use_gamepad_version=pick_ban_use_gamepad_version,
            enable_ready_manager=enable_ready_manager,
        )

        self._ready_minimum_team_size = ready_minimum_team_size

    def as_jsonable_dict(self) -> dict:
        plugin_settings = super().as_jsonable_dict()
        plugin_settings["S_ReadyMinimumTeamSize"] = self._ready_minimum_team_size
        
        return plugin_settings
