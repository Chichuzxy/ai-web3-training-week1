// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import {Script, console} from "forge-std/Script.sol";
import {Halo2Verifier} from "../src/Verifier.sol";

contract DeployVerifier is Script {
    function run() external {
        vm.startBroadcast();

        Halo2Verifier verifier = new Halo2Verifier();

        vm.stopBroadcast();

        console.log("Verifier deployed at:", address(verifier));
    }
}
