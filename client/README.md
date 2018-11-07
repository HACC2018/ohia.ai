# ohia.ai App Client

This README has multiple steps between installation and execution instructions. There are three ways you can follow the steps:
1. Follow all the steps in order as written if you would like to run the client on your browser, the iOS simulator, and an iOS device.
1. Or you can follow, in order as written, *only* the **required** and **browser** steps if you would like to run the client on your browser.
1. Lastly, you can choose the second option for now, and then later on, you can install the **iOS**-specific steps, in order as written.

## Table of Contents

* [Requirements](#requirements)
* [Installation](#installation)
    * [Install Python](#install-python-required)
    * [Install Node.js](#install-nodejs-required)
* [Execution](#execution)
* [New Project Setup](#new-project-setup)
* [Troubleshooting](#troubleshooting)

## Requirements

1. [Python](https://www.python.org/) version 2.7.x
1. [Node.js](https://nodejs.org/en/) version 10.12.0

### Requirements for deploying to an iOS device

1. macOS Mojave version 10.14
1. Xcode version 10.0
1. iPhone 6 running on iOS version 12.0.1

## Installation

### Install Python (required)
1. Download and install Anaconda or Miniconda: https://conda.io/docs/user-guide/install/download.html.
1. In a terminal, create a new conda environment for Python 2.7: `conda create --name python2 python=2.7`.
1. Activate the current terminal window to use the conda environment: `source activate python2`.

### Install Node.js (required)
1. Install [Node Version Manager](https://github.com/creationix/nvm) by running the following in a terminal:
    ```
    curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash
    ```
1. Install Node version 10.12.0 by running: `nvm install 10.12.0`.

### Install Vue.js and Quasar (required)
1. Install Vue CLI: `npm install -g @vue/cli`.
1. Install Vue CLI addon: `npm install -g @vue/cli-init`.
1. Install Quasar CLI: `npm install -g quasar-cli`.

### Install XCode and Cordova (iOS)
1. Download Xcode from the App Store.
1. Enable Xcode CLI tools: `xcode-select --install`.
1. Install Apache Cordova: `npm install -g cordova`.
1. Launch iOS apps from the CLI: `npm install -g ios-deploy`.

### Create the Quasar folder (required)
1. This step is only required when creating the `/client` folder for the first time. See **New Project Setup: Create the Quasar folder** below.

### Create the Cordova folder (iOS)
1. This step is only required when creating the `/client/src-cordova` folder for the first time. See **New Project Setup: Create the Cordova folder** below.

### Check that Cordova is properly installed (iOS)
1. Check that ios got installed: `cordova platform ls`.
1. Verify that Cordova is set up properly: `cordova requirements`.

### Install the client project dependencies (required)
1. From the project root directory, install client dependencies: `npm run install:client` (or you may use [yarn](https://yarnpkg.com/en/docs/install#windows-stable) instead).

### Run the app in the browser (browser)
1. Follow **Execution: Source Environment Variables** below.
1. Follow **Execution: Run the app in the browser** below.

### Run the app in the iOS simulator (iOS)
1. Follow **Execution: Source Environment Variables** below.
1. Follow **Execution: Run the app in the iOS simulator** below.

### Run the app on your iOS device (iOS)
1. Follow **Execution: Source Environment Variables** below.
1. Follow **Execution: Run the app on your iOS device** below.

## Execution

### Source Environment Variables
1. If you haven't done so already, in the client terminal window and from the project root directory, create a `.env` file by copying the template in `.env.sample`.
1. Source your environment by running: `source .env`.
1. You should now see these variables in your environment by running `env`.

### Run the app in the browser (browser)
1. Run `npm run dev` to view the app in a browser.

### Run the app in the iOS simulator (iOS)

#### Development
1. Run the following command to dev in the iOS simulator: `npm run dev-ios`. Make changes to a file and see your changes appear instantaneously in the simulator.

#### Production
1. Run the following command to create a distribution for iOS: `npm run prod-ios`.
1. In the terminal (or you can manually open the file instead), open the Xcode project workspace by running:
    ```
    open ./client/src-cordova/platforms/ios/ohia.ai.xcworkspace/
    ```
1. In Xcode, with the project workspace now open, select a device in the top left-hand corner, such as the `iPhone 6`, and then click the play button icon to run the project in the simulator.

### Run the app on your iOS device (iOS)

**Note that this app was optimized for an iPhone 6 running on iOS version 12.0.1. It was made to be run by Xcode version 10.0 running on macOS Mojave version 10.14. If you experience other problems below, it may be due to versioning issues. Check the [Troubleshooting](#troubleshooting) section first.**

1. If you do not have Mojave, you will need to upgrade your macOS through the App Store.
1. Then you will need to upgrade your Xcode to version 10.0, for compatibility with running iOS version 12.0.1.
1. Then when you're ready, in a terminal window, run the following command to create a distribution for iOS: `npm run prod-ios`. This will generate the following folders in `/client/src-cordova`:
    - `node_modules`
    - `platforms`
    - `plugins`
    - `www`
1. You will see the following, slightly above the tail end of the long output. Notice that the project is built for the iPhone XS Max Simulator. However, we will change this to build for an iPhone device.
    ```
    Building for iPhone XS Max Simulator
    Building project: ~/ohia.ai/client/src-cordova/platforms/ios/ohia.ai.xcworkspace
      Configuration: Release
      Platform: emulator
    Build settings from command line:
        CONFIGURATION_BUILD_DIR = ~/ohia.ai/client/src-cordova/platforms/ios/build/emulator
        SDKROOT = iphonesimulator12.0
        SHARED_PRECOMPS_DIR = ~/ohia.ai/client/src-cordova/platforms/ios/build/sharedpch

    Build settings from configuration file '~/ohia.ai/client/src-cordova/platforms/ios/cordova/build-release.xcconfig':
        CLANG_ALLOW_NON_MODULAR_INCLUDES_IN_FRAMEWORK_MODULES = YES
        CODE_SIGN_ENTITLEMENTS = $(PROJECT_DIR)/$(PROJECT_NAME)/Entitlements-$(CONFIGURATION).plist
        CODE_SIGN_IDENTITY = iPhone Distribution
        ENABLE_BITCODE = NO
        HEADER_SEARCH_PATHS = "$(TARGET_BUILD_DIR)/usr/local/lib/include" "$(OBJROOT)/UninstalledProducts/include" "$(OBJROOT)/UninstalledProducts/$(PLATFORM_NAME)/include" "$(BUILT_PRODUCTS_DIR)"
        OTHER_LDFLAGS = -ObjC
        SWIFT_OBJC_BRIDGING_HEADER = $(PROJECT_DIR)/$(PROJECT_NAME)/Bridging-Header.h

     Build succeeded
    ```
1. In the terminal (or you can manually open the file instead), open the Xcode project workspace by running:
    ```
    open ./client/src-cordova/platforms/ios/ohia.ai.xcworkspace/
    ```
1. Change to the Legacy Build System, since Xcode 10 has issues with the New Build System: https://stackoverflow.com/questions/53050108/xcode-10-how-to-switch-to-old-build-system.
1. Connect your phone via USB to your Mac. Ensure that you see the charge signal next to the battery on your device, and that Xcode recognizes your device (see below that the device is recognized).
    ![alt change_device](https://s3-us-west-2.amazonaws.com/ohia.ai/README/change_device.png)
1. In Xcode, with the project workspace now open, select your device in the top left-hand corner (as in the image above).
1. To run the project, follow the steps in the GIF below (reload this page if you would like to restart the GIF, which lasts a few minutes):
    ![alt run_project](https://s3-us-west-2.amazonaws.com/ohia.ai/README/run_project.gif)
    1. Attempt to run the project by pressing the Play button. You should see a build error as follows: `Signing for "ohia.ai" requires a development team.`
    1. Click on the leftmost (folder) icon in the top left-hand corner, and under the General tab, under the Signing section, ensure that "Automatically manage signing" is checked. Below it, next to Team, select your development team.
    1. If you don't have a development team, you will need to add your Apple ID to Xcode by going to the Xcode toolbar and clicking on Xcode > Preferences.... Then click on the Accounts tab and add your Apple ID by clicking on the + icon.
    1. Not shown in the GIF but a picture is below, for reference: Click on the Manage Certificates... button after you have added your Apple ID. Your signing certificate should include an iOS Development Certificate. If not, you need to click on the + icon dropdown button and select iOS Development and continue from there.
        ![alt manage_certificates](https://s3-us-west-2.amazonaws.com/ohia.ai/README/manage_certificates.png)
    1. After you successfully see an iOS Development Certificate listed when managing certificates, close out of all the modal windows, including Xcode preferences.
    1. Go back to the General tab in the main project (center) panel, if it's not already open.
    1. You should now be able to select your development team under the Signing section.
    1. Ensure that your iPhone is unlocked, then click on the Play button again in Xcode. The installation should run successfully this time (you will see the ohia.ai app with the default iOS robot icon deployed to your phone); however the message `Could not launch "ohia.ai"` should appear in Xcode.
    1. On your iPhone device, follow the instructions from the Xcode modal (click on the step numbers for an image reference, if needed): Go to Settings > General [1](https://s3-us-west-2.amazonaws.com/ohia.ai/README/trust_step_1.png) > Scroll down to Device Management and select it [2](https://s3-us-west-2.amazonaws.com/ohia.ai/README/trust_step_2.png) > Select the developer app (it should show your email) [3](https://s3-us-west-2.amazonaws.com/ohia.ai/README/trust_step_3.png) > Select `Trust "your email here"` [4](https://s3-us-west-2.amazonaws.com/ohia.ai/README/trust_step_4.png) > Select Trust on the modal [5](https://s3-us-west-2.amazonaws.com/ohia.ai/README/trust_step_5.png). Then exit out of Settings.
    1. While your iPhone is still unlocked, go back to Xcode and click on the Play button for the third time. It should now run successfully and you should see output in the console, which will appear on the bottom of the center panel. It should also launch the ohia.ai app on your iPhone.
        ![alt dev_output](https://s3-us-west-2.amazonaws.com/ohia.ai/README/dev_output.png)

## New Project Setup

### Create the Quasar folder (required)
1. From the root directory of this project, type: `quasar init client`.
    ```
    ▶ quasar init frontend
     Running command: vue init 'quasarframework/quasar-starter-kit' frontend

    ? Project name (internal usage for dev) ohia.ai
    ? Project product name (official name) ohia.ai
    ? Project description An open Hawaiian indigenous plant identification and aggre
    gation application.
    ? Author Team ohia.ai of HACC 2018
    ? Check the features needed for your project: ESLint
    ? Pick an ESLint preset Airbnb
    ? Cordova id (disregard if not building mobile apps) org.ohia.ai.app
    ? Should we run `npm install` for you after the project has been created? (recom
    mended) no
    ```

### Create the Cordova folder (iOS)
1. Change into the `/client` folder.
1. Add Cordova Quasar Mode to the Quasar `/client` folder: `quasar mode -a cordova`.
1. Change into the newly generated `/client/src-cordova` folder.
1. Add a Cordova platform (can also replace `ios` with `android`): `cordova platform add ios`.

## Troubleshooting

### Code Signing Error: ohia.ai has conflicting provisioning settings

1. If you keep getting this error when running `npm run prod-ios`:
    ```
    Code Signing Error: ohia.ai has conflicting provisioning settings. ohia.ai is automatically signed for development, but a conflicting code signing identity iPhone Distribution has been manually specified. Set the code signing identity value to "iPhone Developer" in the build settings editor, or switch to manual signing in the project editor.
    Code Signing Error: Code signing is required for product type 'Application' in SDK 'iOS 12.0'
    ```
1. Open the file `/client/src-cordova/platforms/ios/cordova/build-release.xcconfig` and change from:
    ```
    CODE_SIGN_IDENTITY = iPhone Distribution
    CODE_SIGN_IDENTITY[sdk=iphoneos*] = iPhone Distribution
    ```
    to:
    ```
    CODE_SIGN_IDENTITY = iPhone Developer
    CODE_SIGN_IDENTITY[sdk=iphoneos*] = iPhone Developer
    ```
1. Then run `npm run prod-ios` again.

