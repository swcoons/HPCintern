
n tryRequire(pkg)
        require(pkg)
        print(string.format("Successfully loaded '%s'",pkg));
end

function loadCredit()
        local trainFile = hdf5.open('/app/projects/usnadeep/data/credit/credit.h5')
        local trX = trainFile:read('/trainX'):all()
        local trY = trainFile:read('/trainY'):all()
        local testFile = hdf5.open('/app/projects/usnadeep/data/credit/credit.h5')
        local teX = testFile:read('/testX'):all()
        local teY = testFile:read('/testY'):all()
        return trX,trY,teX,teY
end

tryRequire('nn')
tryRequire('optim')
tryRequire('hdf5')

trX, trY, teX, teY = loadCredit()

print (teX:size())

