# big numbers generator
docker run --rm -v $(pwd):/src -v /home/osboxes/secLibFroWasm:/home/osboxes/secLibFroWasm -u 1000 trzeci/emscripten emcc -O3 BigNumbers/BigNumbersAPI.cpp BigNumbers/BigNumbers.cpp BigNumbers/BigNumbersImpl.cpp -o BigNumbers.js -s EXPORTED_FUNCTIONS='["_BNRandomHex", "_BNRandomDec","_BNRandomHexWithSeed","_BNRandomDecWithSeed","_addFromDec","_addFromHex","_subFromHex","_subFromDec"]' -s EXTRA_EXPORTED_RUNTIME_METHODS='["ccall", "cwrap"]' -I. -I/home/osboxes/secLibFroWasm -I/home/osboxes/secLibFroWasm/openssl/include -L/home/osboxes/secLibFroWasm/openssl -std=c++11 -g -pthread -lssl -lcrypto

# MessageHash generator
docker run --rm -v $(pwd):/src -v /home/osboxes/secLibFroWasm:/home/osboxes/secLibFroWasm -u 1000 trzeci/emscripten emcc -O3 MessageHash/MessageHashAPI.cpp MessageHash/MessageHash.cpp MessageHash/MessageHashImpl.cpp -o MessageHash.js -s EXPORTED_FUNCTIONS='["_HashMsgSHA256", "_HashMsg","_ListHashFunc"]' -s EXTRA_EXPORTED_RUNTIME_METHODS='["ccall", "cwrap"]' -I. -I/home/osboxes/secLibFroWasm -I/home/osboxes/secLibFroWasm/openssl/include -L/home/osboxes/secLibFroWasm/openssl -std=c++11 -g -pthread -lssl -lcrypto

# Combine all into one lib
docker run --rm -v $(pwd):/src -v /home/osboxes/secLibFroWasm:/home/osboxes/secLibFroWasm -u 1000 trzeci/emscripten emcc -O3 MessageHash/MessageHashAPI.cpp MessageHash/MessageHash.cpp MessageHash/MessageHashImpl.cpp BigNumbers/BigNumbersAPI.cpp BigNumbers/BigNumbers.cpp BigNumbers/BigNumbersImpl.cpp -o CryptoBase.js -s EXPORTED_FUNCTIONS='["_HashMsgSHA256", "_HashMsg","_ListHashFunc","_BNRandomHex", "_BNRandomDec","_BNRandomHexWithSeed","_BNRandomDecWithSeed","_addFromDec","_addFromHex","_subFromHex","_subFromDec"]' -s EXTRA_EXPORTED_RUNTIME_METHODS='["ccall", "cwrap"]' -I. -I/home/osboxes/secLibFroWasm -I/home/osboxes/secLibFroWasm/openssl/include -L/home/osboxes/secLibFroWasm/openssl -std=c++11 -g -pthread -lssl -lcrypto


docker run --rm -v $(pwd):/src -v /home/osboxes/secLibFroWasm:/home/osboxes/secLibFroWasm -u 1000 trzeci/emscripten emcc -O3 sdklibraries/src/core/MessageHash/MessageHashAPI.cpp sdklibraries/src/core/MessageHash/MessageHash.cpp sdklibraries/src/core/MessageHash/MessageHashImpl.cpp sdklibraries/src/core/MessageHash/Base64EncDec.cpp sdklibraries/src/core/MessageHash/Base64EncDecImpl.cpp sdklibraries/src/core/MessageHash/Base58EncDec.cpp sdklibraries/src/core/MessageHash/Base58EncDecImpl.cpp sdklibraries/src/core/BigNumbers/BigNumbersAPI.cpp sdklibraries/src/core/BigNumbers/BigNumbers.cpp sdklibraries/src/core/BigNumbers/BigNumbersImpl.cpp -o CryptoBase.js -s EXPORTED_FUNCTIONS='["_HashMsgSHA256", "_HashMsg","_ListHashFunc","_EncodeBase64", "_DecodeBase64", "_BNRandomHex", "_BNRandomDec","_BNRandomHexWithSeed","_BNRandomDecWithSeed","_addFromDec","_addFromHex","_subFromHex","_subFromDec"]' -s EXTRA_EXPORTED_RUNTIME_METHODS='["ccall", "cwrap"]' -I. -I./sdklibraries/src/core -I./build/generated_hpp -I/home/osboxes/secLibFroWasm -I/home/osboxes/secLibFroWasm/openssl/include -L/home/osboxes/secLibFroWasm/openssl -std=c++11 -g -pthread -lssl -lcrypto


docker run --rm -v $(pwd):/src -v /home/osboxes/secLibFroWasm:/home/osboxes/secLibFroWasm -u 1000 trzeci/emscripten emcc -O3 tweetnacl.c sss.c randombytes/randombytes.c  hazmat.c wrapper.c -o sss.js -s EXPORTED_FUNCTIONS='["_create_shares", "_combine_shares","_create_keyshares","_create_keyshares"]' -s EXTRA_EXPORTED_RUNTIME_METHODS='["ccall", "cwrap"]' -I. -I/home/osboxes/secLibFroWasm -I/home/osboxes/secLibFroWasm/openssl/include -L/home/osboxes/secLibFroWasm/openssl -g -pthread -lssl -lcrypto

<THIS IS WHERE I WAS AT ON SUNDAY 12/05>
docker run --rm -v $(pwd):/src -v /home/osboxes/secLibFroWasm:/home/osboxes/secLibFroWasm -u 1000 trzeci/emscripten emcc -O3 sdklibraries/src/core/MessageHash/MessageHashAPI.cpp sdklibraries/src/core/MessageHash/MessageHash.cpp sdklibraries/src/core/MessageHash/MessageHashImpl.cpp sdklibraries/src/core/MessageHash/Base64EncDec.cpp sdklibraries/src/core/MessageHash/Base64EncDecImpl.cpp sdklibraries/src/core/MessageHash/Base58EncDec.cpp sdklibraries/src/core/MessageHash/Base58EncDecImpl.cpp sdklibraries/src/core/BigNumbers/BigNumbersAPI.cpp sdklibraries/src/core/BigNumbers/BigNumbers.cpp sdklibraries/src/core/BigNumbers/BigNumbersImpl.cpp sdklibraries/src/core/utils/emscriptBindings.cpp --bind -o CryptoBase.js -s WASM=1 -s EXPORTED_FUNCTIONS='["_HashMsgSHA256", "_HashMsg","_EncodeBase64", "_DecodeBase64", "_BNRandomHex", "_BNRandomDec","_BNRandomHexWithSeed","_BNRandomDecWithSeed","_addFromDec","_addFromHex","_subFromHex","_subFromDec"]' -s EXTRA_EXPORTED_RUNTIME_METHODS='["ccall", "cwrap"]' -I. -I./sdklibraries/src/core -I./build/generated_hpp -I/home/osboxes/secLibFroWasm -I/home/osboxes/secLibFroWasm/openssl/include -L/home/osboxes/secLibFroWasm/openssl -std=c++1^C-g -pthread -lssl -lcrypto



docker run --rm -v $(pwd):/src -v /home/osboxes/secLibFroWasm:/home/osboxes/secLibFroWasm -u 1000 trzeci/emscripten emcc -O3 MarshallData.cpp  --bind -o TestData.js  -s WASM=1 -s EXPORTED_FUNCTIONS='["_TakeUint8Data"]' -s EXTRA_EXPORTED_RUNTIME_METHODS='["ccall", "cwrap"]' -I.  -L/home/osboxes/secLibFroWasm/openssl -std=c++11 -g -pthread -lssl -lcrypto

