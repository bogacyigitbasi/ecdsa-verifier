// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";
import "@openzeppelin/contracts/utils/cryptography/MessageHashUtils.sol";
contract Verifier {
    using ECDSA for bytes32;
    using MessageHashUtils for bytes32;
    address public verifyingAddress;
    constructor(address _verifyingAddress) {
        verifyingAddress = _verifyingAddress;
    }
    // send the message and create hash and sign
    function verifyV1(
        string calldata message,
        bytes32 r,
        bytes32 s,
        uint8 v
    ) public view {
        bytes32 signedMessageHash = keccak256(abi.encode(message))
            .toEthSignedMessageHash();
        //
        require(
            signedMessageHash.recover(v, r, s) == verifyingAddress,
            "invalid signature"
        );
    }

    function verifyV2(
        string calldata message,
        bytes calldata signature
    ) public view {
        bytes32 signedMessage = keccak256(abi.encode(message));
        require(
            signedMessage.recover(signature) == verifyingAddress,
            "invalid signature"
        );
    }
}
