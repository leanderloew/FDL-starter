const dotenv = require('dotenv');

module.exports = async ({ options, resolveConfigurationProperty }) => {
  // Load env vars into Serverless environment
  // You can do more complicated env var resolution with dotenv here

  if (options.stage === "dev")
  {
    var file_name = '../.envs/dev.env'
  }else{
    var file_name = '../.envs/prod.env'
  }

  const envVars = dotenv.config({ path: file_name }).parsed;
  var env_1 =  Object.assign(
    {},
    envVars,
  );
  const envVars2 = dotenv.config({ path: '../.envs/gen.env' }).parsed;
  var env_2=  Object.assign(
    {},
    envVars2,
  );
  env_3 = {...env_1, ...env_2}

  delete env_3["AWS_ACCESS_KEY_ID"]
  delete env_3["AWS_SECRET_ACCESS_KEY"]

  // making sure remote variables are used
  env_3["IS_LOCAL"] = "False"

  return env_3
};