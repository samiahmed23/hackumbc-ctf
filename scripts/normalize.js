(function(global){
	'use strict';
	const ZERO_WIDTH = /[\u200B\u200C\u200D\u2060\uFEFF]/g; // ZWSP, ZWNJ, ZWJ, WJ, BOM
	function normalizeNFKCAndStripZWs(input){
		if (!input) return '';
		try{
			return input.normalize('NFKC').replace(ZERO_WIDTH, '');
		}catch(e){
			// Older engines: fallback to identity replace
			return (''+input).replace(ZERO_WIDTH, '');
		}
	}
	global.normalizeNFKCAndStripZWs = normalizeNFKCAndStripZWs;
})(window);

