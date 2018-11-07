# ohia.ai App Client

This README has a lot of steps between installation and running instructions. There are three ways you can follow the steps:
1. Follow all the steps in order as written if you would like to run the client on your browser and the iOS simulator.
1. Or you can follow, in order as written, *only* the **required** and **browser** steps if you would like to run the client on your browser.
1. Lastly, you can choose the second option for now, and then later on, you can install the **iOS**-specific steps, in order as written.

## Requirements

1. [Node.js](https://nodejs.org/en/) version 10.12.0

## Installation

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
1. See **Running: Run the app in the browser** below.

### Run the app in the iOS simulator (iOS)
1. See **Running: Run the app in the iOS simulator** below.

### Run the app on your iOS device (iOS)
1. See **Running: Run the app on your iOS device** below.

## Running

### Run the client Quasar project in the browser (browser)
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
1. Run the following command to create a distribution for iOS: `npm run prod-ios`.
1. In the terminal (or you can manually open the file instead), open the Xcode project workspace by running:
    ```
    open ./client/src-cordova/platforms/ios/ohia.ai.xcworkspace/
    ```
1. Connect your phone TODO
1. In Xcode, with the project workspace now open, select a device in the top left-hand corner, such as the `iPhone 6`, and then click the play button icon to run the project in the simulator.

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
