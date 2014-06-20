Vagrant.configure("2") do |config|
  ## Choose your base box
  config.vm.box = "precise64"

  config.vm.synced_folder "", "/home/vagrant/celery-demo"

  config.vm.network "forwarded_port", guest: 8000, host: 9000
  config.ssh.forward_agent = true

  config.vm.host_name = 'celery-1'
end
