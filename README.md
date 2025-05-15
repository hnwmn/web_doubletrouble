**A basic parameter pollution vulnerability lab, originally created for personal use and later adapted as one of the CTF challenges at the misc0nfig conference.**

## Category: Web

## Description

Welcome to our store! We're selling the legendary Nokia 3310 for £199. Can you find a way to get it for less?

## Flag: 
GooseCTF{parametr_p0lluti0n_dtctd}

Solution:

The challenge involves a HTTP parameter pollution vulnerability. This is a web vulnerability where different back-end technologies handle multiple parameters with the same name differently (see more here: [https://en.wikipedia.org/wiki/HTTP_parameter_pollution](https://en.wikipedia.org/wiki/HTTP_parameter_pollution)). In this case, the application takes the last price parameter submitted and checks if multiple price parameters were sent.

To solve, send a request like: `/checkout?price=199&price=1`. The first price parameter will be used for the actual price check, and the second price parameter will trigger the multiple parameters detection.

Previous Challenge: N/A