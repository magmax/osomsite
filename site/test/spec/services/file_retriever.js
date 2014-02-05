'use strict';

describe('Service: FileRetriever', function () {

  // load the service's module
  beforeEach(module('siteApp'));

  // instantiate service
  var FileRetriever;
  beforeEach(inject(function (_FileRetriever_) {
    FileRetriever = _FileRetriever_;
  }));

  it('should do something', function () {
    expect(!!FileRetriever).toBe(true);
  });

});
