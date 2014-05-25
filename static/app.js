var app = angular.module("app", ['ngResource']);

app.controller("controller", ['$scope', '$resource', function($scope, $resource){
    var Things = $resource("/things");
    $scope.things = [];

    $scope.load = function(){
        $scope.things = Things.query();
    }
}]);