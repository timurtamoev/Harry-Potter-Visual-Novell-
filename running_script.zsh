mkdir -p out/production/project
javac -d out/production/project src/*.java
java -cp out/production/project Main
echo "success"
