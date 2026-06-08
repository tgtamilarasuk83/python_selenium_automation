from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

AD_DOMAINS = [
    "googlesyndication.com",
    "doubleclick.net",
    "adservice.google.com",
    "googletagservices.com",
    "googletagmanager.com",
    "google-analytics.com",
    "pagead2.googlesyndication.com",
    "tpc.googlesyndication.com",
    "adclick.g.doubleclick.net",
    "securepubads.g.doubleclick.net",
]

def enable_network_ad_blocking(driver):
    driver.execute_cdp_cmd("Network.enable", {})
    driver.execute_cdp_cmd("Network.setBlockedURLs", {"urls": AD_DOMAINS})
    print("[AdGuard] CDP network blocking enabled.")

def close_new_tab_ads(driver):
    if len(driver.window_handles) > 1:
        main_window = driver.window_handles[0]
        for handle in driver.window_handles[1:]:
            driver.switch_to.window(handle)
            driver.close()
        driver.switch_to.window(main_window)

def dismiss_ad_overlays(driver):
    close_selectors = [
        "//div[@id='ad_position_box']//a[contains(@onclick,'close')]",
        "//a[@id='dismiss-button']",
        "//*[contains(@class,'modal')]//button[contains(text(),'Close')]",
        "//*[contains(@class,'modal')]//button[contains(@class,'close')]",
    ]
    for xpath in close_selectors:
        try:
            btn = driver.find_element(By.XPATH, xpath)
            if btn.is_displayed():
                driver.execute_script("arguments[0].remove();", btn)
        except NoSuchElementException:
            pass

def block_ads(driver):
    close_new_tab_ads(driver)
    dismiss_ad_overlays(driver)
    driver.execute_script("""
        document.querySelectorAll('iframe').forEach(el => {
            if (el.src && (el.src.includes('googlesyndication') ||
                           el.src.includes('doubleclick') ||
                           el.src.includes('adservice') ||
                           el.src.includes('googletagmanager'))) {
                el.remove();
            }
        });
        document.querySelectorAll(
            '.adsbygoogle, [id*="google_ads"], [id*="ad_"], [class*="ad-banner"], ins'
        ).forEach(el => el.remove());
    """)