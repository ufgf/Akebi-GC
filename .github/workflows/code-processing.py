# pylint: disable=C0114:missing-docstring, C0301:line-too-long, C0103:invalid-name, R1727:condition-evals-to-constant, W1514:unspecified-encoding, W0703:broad-except

# don't blame me for so low-quality code ¯\_(ツ)_/¯
print("- Making some changes to sources...")


try:
    with open('cheat-library/cheat-library.vcxproj', 'r+', newline="") as f:
        print("• 1/2: comment out CustomBuildStep sections...")
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            if '<CustomBuildStep>' or '</CustomBuildStep>' in line:
                line = line.replace('<CustomBuildStep>', '<!-- <CustomBuildStep>').replace('</CustomBuildStep>', '</CustomBuildStep> -->')
                f.write(line)
except Exception as e:
    print(f"...unsuccessful, reason: {e}")
print("...successful")


try:
    with open('.gitmodules', 'a', newline="") as f:
        print("• 2/2: adding protobuf to .gitmodules...")
        f.write("[submodule \"cheat-library/vendor/protobuf\"]\n\
	path = cheat-library/vendor/protobuf\n\
	url = https://github.com/protocolbuffers/protobuf.git\n")
except Exception as e:
    print(f"...unsuccessful, reason: {e}")
print("...successful")
