import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import scienceplots
plt.style.use(["science", "grid", "notebook"])

sys.path.append("/home/dkk/work/remote/grand")
from grand.io.root_trees import *

from pprint import pprint
from loguru import logger
logger.level='INFO'

rootfile = sys.argv[1]
dirname = os.path.dirname(rootfile)
basename = os.path.basename(rootfile)
if not os.path.exists(f"figure_{basename[:-5]}"):
    os.mkdir(f"figure_{basename[:-5]}")

print(f"Reading file {rootfile}")
trun = RunTree(rootfile)
# tshower = ShowerEventTree(rootfile)
# tvoltage = VoltageEventTree(rootfile)
tadc = ADCEventTree(rootfile)

# pprint(dir(trun))
# pprint(dir(tshower))
# pprint(dir(tvoltage))
# pprint(dir(tadc))
# exit()

data_generator          = trun.data_generator
data_generator_version  = trun.data_generator_version
data_source             = trun.data_source
first_event             = trun.first_event
first_event_time        = trun.first_event_time
last_event              = trun.last_event
last_event_time         = trun.last_event_time
origin_geoid            = trun.origin_geoid
run_mode                = trun.run_mode
run_number              = trun.run_number
site                    = trun.site
site_lat                = trun.site_lat
site_long               = trun.site_long
tree                    = trun.tree
tree_name               = trun.tree_name
logger.debug(f"data_generator:          {data_generator}")
logger.debug(f"data_generator_version:  {data_generator_version}")
logger.debug(f"data_source:             {data_source}")
logger.debug(f"first_event:             {first_event}")
logger.debug(f"first_event_time:        {first_event_time}")
logger.debug(f"last_event:              {last_event}")
logger.debug(f"last_event_time:         {last_event_time}")
logger.debug(f"origin_geoid:            {origin_geoid}")
logger.debug(f"run_mode:                {run_mode}")
logger.debug(f"run_number:              {run_number}")
logger.debug(f"site:                    {site}")
logger.debug(f"site_lat:                {site_lat}")
logger.debug(f"site_long:               {site_long}")
logger.debug(f"tree:                    {tree}")
logger.debug(f"tree_name:               {tree_name}")
# exit()

# Print out the list of runs,events
# tshower.print_list_of_events()
# tvoltage.print_list_of_events()
tadc.print_list_of_events()

event_number = tadc.get_number_of_events()
logger.info(f'event_number: {event_number}')

# Get the list of runs,events
list_of_events = tadc.get_list_of_events()

for du in ['1031', '1035', '1078', '1080', '1081', '1082', '1094']:
    exec(f'times_{du} = []')
    for i in range(4):
        exec(f'means_{i}_{du} = []')
        exec(f'stds_{i}_{du} = []')


# Read the first event from the list of events
for event in list_of_events:
    tadc.get_event(*event)
    acceleration_x = tadc.acceleration_x
    acceleration_y = tadc.acceleration_y
    acceleration_z = tadc.acceleration_z
    logger.debug(f"acceleration_x: {acceleration_x}")
    logger.debug(f"acceleration_y: {acceleration_y}")
    logger.debug(f"acceleration_z: {acceleration_z}")

    adc_enabled_channels = tadc.adc_enabled_channels
    adc_input_channels = tadc.adc_input_channels
    logger.debug(f"adc_enabled_channels: {adc_enabled_channels}")
    logger.debug(f"adc_input_channels: {adc_input_channels}")

    adc_samples_count_channel0 = tadc.adc_samples_count_channel0
    adc_samples_count_channel1 = tadc.adc_samples_count_channel1
    adc_samples_count_channel2 = tadc.adc_samples_count_channel2
    adc_samples_count_channel3 = tadc.adc_samples_count_channel3
    adc_samples_count_total = tadc.adc_samples_count_total
    logger.debug(f"adc_samples_count_channel0: {adc_samples_count_channel0}")
    logger.debug(f"adc_samples_count_channel1: {adc_samples_count_channel1}")
    logger.debug(f"adc_samples_count_channel2: {adc_samples_count_channel2}")
    logger.debug(f"adc_samples_count_channel3: {adc_samples_count_channel3}")
    logger.debug(f"adc_samples_count_total: {adc_samples_count_total}")

    adc_sampling_frequency = tadc.adc_sampling_frequency
    adc_sampling_resolution = tadc.adc_sampling_resolution
    logger.debug(f"adc_sampling_frequency: {adc_sampling_frequency}")
    logger.debug(f"adc_sampling_resolution: {adc_sampling_resolution}")

    atm_humidity = tadc.atm_humidity
    atm_pressure = tadc.atm_pressure
    atm_temperature = tadc.atm_temperature
    battery_level = tadc.battery_level
    logger.debug(f"atm_humidity: {atm_humidity}")
    logger.debug(f"atm_pressure: {atm_pressure}")
    logger.debug(f"atm_temperature: {atm_temperature}")
    logger.debug(f"battery_level: {battery_level}")

    channel_properties0 = tadc.channel_properties0
    channel_properties1 = tadc.channel_properties1
    channel_properties2 = tadc.channel_properties2
    channel_properties3 = tadc.channel_properties3
    logger.debug(f"channel_properties0: {channel_properties0}")
    logger.debug(f"channel_properties1: {channel_properties1}")
    logger.debug(f"channel_properties2: {channel_properties2}")
    logger.debug(f"channel_properties3: {channel_properties3}")

    channel_trig_settings0 = tadc.channel_trig_settings0
    channel_trig_settings1 = tadc.channel_trig_settings1
    channel_trig_settings2 = tadc.channel_trig_settings2
    channel_trig_settings3 = tadc.channel_trig_settings3
    logger.debug(f"channel_trig_settings0: {channel_trig_settings0}")
    logger.debug(f"channel_trig_settings1: {channel_trig_settings1}")
    logger.debug(f"channel_trig_settings2: {channel_trig_settings2}")
    logger.debug(f"channel_trig_settings3: {channel_trig_settings3}")

    clock_tick = tadc.clock_tick
    clock_ticks_per_second = tadc.clock_ticks_per_second
    logger.debug(f"clock_tick: {clock_tick}")
    logger.debug(f"clock_ticks_per_second: {clock_ticks_per_second}")

    du_id = tadc.du_id
    first_du = tadc.first_du
    du_count = tadc.du_count
    du_seconds = tadc.du_seconds
    du_nanoseconds = tadc.du_nanoseconds
    logger.info(f"du_id: {du_id}")
    logger.debug(f"first_du: {first_du}")
    logger.debug(f"du_count: {du_count}")
    logger.debug(f"du_seconds: {du_seconds}")
    logger.debug(f"du_nanoseconds: {du_nanoseconds}")

    event_id = tadc.event_id
    event_number = tadc.event_number
    event_size = tadc.event_size
    event_type = tadc.event_type
    event_version = tadc.event_version
    logger.debug(f"event_id: {event_id}")
    logger.debug(f"event_number: {event_number}")
    logger.debug(f"event_size: {event_size}")
    logger.debug(f"event_type: {event_type}")
    logger.debug(f"event_version: {event_version}")

    gps_alarms = tadc.gps_alarms
    gps_alt = tadc.gps_alt
    gps_lat = tadc.gps_lat
    gps_leap_second = tadc.gps_leap_second
    gps_long = tadc.gps_long
    gps_offset = tadc.gps_offset
    gps_status = tadc.gps_status
    gps_temp = tadc.gps_temp
    gps_time = tadc.gps_time
    gps_warnings = tadc.gps_warnings
    logger.debug(f"gps_alarms: {gps_alarms}")
    logger.debug(f"gps_alt: {gps_alt}")
    logger.debug(f"gps_lat: {gps_lat}")
    logger.debug(f"gps_leap_second: {gps_leap_second}")
    logger.debug(f"gps_long: {gps_long}")
    logger.debug(f"gps_offset: {gps_offset}")
    logger.debug(f"gps_status: {gps_status}")
    logger.info(f"gps_temp: {gps_temp}")
    logger.info(f"gps_time: {gps_time}")
    logger.debug(f"gps_warnings: {gps_warnings}")

    run_number = tadc.run_number
    t3_number = tadc.t3_number
    time_nanoseconds = tadc.time_nanoseconds
    time_seconds = tadc.time_seconds
    logger.debug(f"run_number: {run_number}")
    logger.debug(f"t3_number: {t3_number}")
    logger.debug(f"time_nanoseconds: {time_nanoseconds}")
    logger.debug(f"time_seconds: {time_seconds}")

    trace_0 = np.array(tadc.trace_0)
    trace_1 = np.array(tadc.trace_1)
    trace_2 = np.array(tadc.trace_2)
    trace_3 = np.array(tadc.trace_3)
    logger.debug(f"trace_0: {trace_0.shape}")
    logger.debug(f"trace_1: {trace_1.shape}")
    logger.debug(f"trace_2: {trace_2.shape}")
    logger.debug(f"trace_3: {trace_3.shape}")
    logger.debug(f"mean of trace_0: {np.mean(trace_0, axis=1)}")
    logger.debug(f"mean of trace_1: {np.mean(trace_1, axis=1)}")
    logger.debug(f"mean of trace_2: {np.mean(trace_2, axis=1)}")
    logger.debug(f"mean of trace_3: {np.mean(trace_3, axis=1)}")
    logger.debug(f"deviation of trace_0: {np.std(trace_0, axis=1)}")
    logger.debug(f"deviation of trace_1: {np.std(trace_1, axis=1)}")
    logger.debug(f"deviation of trace_2: {np.std(trace_2, axis=1)}")
    logger.debug(f"deviation of trace_3: {np.std(trace_3, axis=1)}")

    eval(f'times_{du_id[0]}.append(gps_time[1] + gps_time[2]/1e9)')
    eval(f'means_0_{du_id[0]}.append(np.mean(trace_0, axis=1)[0])')
    eval(f'means_1_{du_id[0]}.append(np.mean(trace_1, axis=1)[0])')
    eval(f'means_2_{du_id[0]}.append(np.mean(trace_2, axis=1)[0])')
    eval(f'means_3_{du_id[0]}.append(np.mean(trace_3, axis=1)[0])')
    eval(f'stds_0_{du_id[0]}.append(np.std(trace_0, axis=1)[0])')
    eval(f'stds_1_{du_id[0]}.append(np.std(trace_1, axis=1)[0])')
    eval(f'stds_2_{du_id[0]}.append(np.std(trace_2, axis=1)[0])')
    eval(f'stds_3_{du_id[0]}.append(np.std(trace_3, axis=1)[0])')

    trace_0_fft = np.fft.rfft(trace_0, axis=1)
    trace_1_fft = np.fft.rfft(trace_1, axis=1)
    trace_2_fft = np.fft.rfft(trace_2, axis=1)
    trace_3_fft = np.fft.rfft(trace_3, axis=1)
    logger.debug(f"trace_0_fft.shape: {trace_0_fft.shape}")
    logger.debug(f"trace_1_fft.shape: {trace_1_fft.shape}")
    logger.debug(f"trace_2_fft.shape: {trace_2_fft.shape}")
    logger.debug(f"trace_3_fft.shape: {trace_3_fft.shape}")
    # exit()

    fs = adc_sampling_frequency[0]  # MHz
    fs = 500
    n = adc_samples_count_channel0[0]
    freqs = np.fft.rfftfreq(n, 1 / fs)
    logger.debug(f'freqs: {len(freqs)}')
    # exit()

    t = np.linspace(0, n / (fs * 1e6), n) * 1e6
    # time = gps_time[1] + gps_time[1] / 1e9
    # t = time + t

    # """
    for id, du_number in enumerate(du_id):
        plt.figure()
        plt.subplot(411)
        plt.plot(t, trace_0[id, :], label="Float")
        plt.gca().set_xticklabels([])
        plt.text(1.01, 0.5, "Float", fontsize='larger', transform=plt.gca().transAxes)
        # plt.legend(bbox_to_anchor=(1,1))
        plt.subplot(412)
        plt.plot(t, trace_1[id, :], label="X (NS)")
        plt.gca().set_xticklabels([])
        plt.text(1.01, 0.5, "X (NS)", fontsize='larger', transform=plt.gca().transAxes)
        # plt.legend(bbox_to_anchor=(1,1))
        plt.subplot(413)
        plt.plot(t, trace_2[id, :], label="Y (EW)")
        plt.gca().set_xticklabels([])
        plt.text(1.01, 0.5, "Y (EW)", fontsize='larger', transform=plt.gca().transAxes)
        # plt.legend(bbox_to_anchor=(1,1))
        plt.subplot(414)
        plt.plot(t, trace_3[id, :], label="Z (UD)")
        plt.xlabel("Time ($\mu$s)")
        plt.text(1.01, 0.5, "Z (UD)", fontsize='larger', transform=plt.gca().transAxes)
        # plt.legend(bbox_to_anchor=(1,1))
        plt.savefig(
            f"figure_{basename[:-5]}/trace_{basename[:-5]}_runID{run_number}_evtID{event_number}_duID{du_number}.png"
        )

        plt.figure()
        plt.subplot(411)
        plt.plot(freqs[: n // 2], np.abs(trace_0_fft[id, : n // 2]), label="Float")
        plt.gca().set_xticklabels([])
        plt.yscale("log")
        plt.text(1.01, 0.5, "Float", fontsize='larger', transform=plt.gca().transAxes)
        # plt.legend(bbox_to_anchor=(1,1))
        plt.subplot(412)
        plt.plot(freqs[: n // 2], np.abs(trace_1_fft[id, : n // 2]), label="X (NS)")
        plt.gca().set_xticklabels([])
        plt.yscale("log")
        plt.text(1.01, 0.5, "X (NS)", fontsize='larger', transform=plt.gca().transAxes)
        # plt.legend(bbox_to_anchor=(1,1))
        plt.subplot(413)
        plt.plot(freqs[: n // 2], np.abs(trace_2_fft[id, : n // 2]), label="Y (EW)")
        plt.gca().set_xticklabels([])
        plt.yscale("log")
        plt.text(1.01, 0.5, "Y (EW)", fontsize='larger', transform=plt.gca().transAxes)
        # plt.legend(bbox_to_anchor=(1,1))
        plt.subplot(414)
        plt.plot(freqs[: n // 2], np.abs(trace_3_fft[id, : n // 2]), label="Z (UD)")
        plt.yscale("log")
        plt.text(1.01, 0.5, "Z (UD)", fontsize='larger', transform=plt.gca().transAxes)
        # plt.legend(bbox_to_anchor=(1,1))
        plt.xlabel("Frequency (MHz)")
        plt.savefig(
            f"figure_{basename[:-5]}/fft_trace_{basename[:-5]}_runID{run_number}_evtID{event_number}_duID{du_number}.png"
        )
        # exit()
    # """

    trigger_flag = tadc.trigger_flag
    trigger_pattern = tadc.trigger_pattern
    trigger_position = tadc.trigger_position
    trigger_rate = tadc.trigger_rate
    logger.debug(f"trigger_flag: {trigger_flag}")
    logger.debug(f"trigger_pattern: {trigger_pattern}")
    logger.debug(f"trigger_position: {trigger_position}")
    logger.debug(f"trigger_rate: {trigger_rate}")

for du in ['1031', '1035', '1078', '1080', '1081', '1082', '1094']:
    logger.info(f'times_{du}.shape:',  eval(f'len(times_{du})'))
    plt.figure()
    plt.subplot(411)
    plt.scatter(eval(f'times_{du}'), eval(f'means_0_{du}'), marker='.', s=1)
    plt.gca().set_xticklabels([])
    plt.ylabel('mean of O')
    plt.subplot(412)
    plt.scatter(eval(f'times_{du}'), eval(f'means_1_{du}'), marker='.', s=1)
    plt.gca().set_xticklabels([])
    plt.ylabel('mean of X')
    plt.subplot(413)
    plt.scatter(eval(f'times_{du}'), eval(f'means_2_{du}'), marker='.', s=1)
    plt.gca().set_xticklabels([])
    plt.ylabel('mean of Y')
    plt.subplot(414)
    plt.scatter(eval(f'times_{du}'), eval(f'means_3_{du}'), marker='.', s=1)
    plt.ylabel('mean of Z')
    plt.xlabel('GPS time')
    plt.savefig(f"mean_duID{du}_{basename[:-5]}.png")

    plt.figure()
    plt.subplot(411)
    plt.scatter(eval(f'times_{du}'), eval(f'stds_0_{du}'), marker='.', s=1)
    plt.gca().set_xticklabels([])
    plt.ylabel('RMS of O')
    plt.subplot(412)
    plt.scatter(eval(f'times_{du}'), eval(f'stds_1_{du}'), marker='.', s=1)
    plt.gca().set_xticklabels([])
    plt.ylabel('RMS of X')
    plt.subplot(413)
    plt.scatter(eval(f'times_{du}'), eval(f'stds_2_{du}'), marker='.', s=1)
    plt.gca().set_xticklabels([])
    plt.ylabel('RMS of Y')
    plt.subplot(414)
    plt.scatter(eval(f'times_{du}'), eval(f'stds_3_{du}'), marker='.', s=1)
    plt.ylabel('RMS of Z')
    plt.xlabel('GPS time')
    plt.savefig(f"std_duID{du}_{basename[:-5]}.png")
